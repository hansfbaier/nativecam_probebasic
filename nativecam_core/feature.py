"""
Feature — a CAM operation (circle, rectangle, drill, etc.).

Ported from NativeCAM ncam.py Feature class (lines 1588-1948).
Handles:
- Loading from .cfg files
- Parameter management
- G-code template processing with <eval>, <exec>, <subprocess>, <import>
- Validation
"""

import configparser
import hashlib
import io
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

from .parameter import Parameter, _get_float, _get_int, _get_string
from .preferences import DEFAULT_METRIC, MACHINE_METRIC, DEFAULT_DIGITS

# XML root tag for project files
XML_TAG = "lcnc-ncam"

# Global trackers (mimicking NativeCAM's module-level state)
INCLUDE = set()
DEFINITIONS = set()

# Search path for files (set by the application)
NCAM_DIR = None
SYS_DIR = None
CFG_DIR = 'cfg'
PROJECTS_DIR = 'projects'
LIB_DIR = 'lib'
GRAPHICS_DIR = 'graphics'
CATALOGS_DIR = 'catalogs'
CUSTOM_DIR = 'my-stuff'

# Unique ID counter
UNIQUE_ID = 9


def get_short_id():
    """Generate a short unique hex ID."""
    global UNIQUE_ID
    UNIQUE_ID += 1
    m = hashlib.md5()
    m.update(str(UNIQUE_ID).encode())
    return m.hexdigest()[:4].upper()


def search_path(warn, filename, *path_parts):
    """Search for a file in multiple locations."""
    if not filename:
        return None

    if os.path.isfile(filename):
        return filename

    # Search from NCAM_DIR with optional sub-path
    if NCAM_DIR:
        src = os.path.join(NCAM_DIR, *path_parts, filename)
        src = os.path.abspath(src)
        if os.path.isfile(src):
            return src

    # Search standard subdirectories (relative to CWD, then relative to NCAM_DIR)
    for dirname in [GRAPHICS_DIR, CFG_DIR, CATALOGS_DIR, LIB_DIR, PROJECTS_DIR]:
        # Relative to CWD
        src = os.path.join(dirname, filename)
        if os.path.isfile(src):
            return src
        # Relative to NCAM_DIR
        if NCAM_DIR:
            src = os.path.join(NCAM_DIR, dirname, filename)
            if os.path.isfile(src):
                return src

    # Search current directory
    src = os.path.join(os.getcwd(), filename)
    if os.path.isfile(src):
        return src

    if warn:
        print("Can not find file %s" % filename)

    return None


class Feature:
    """A CAM feature (operation) with parameters and G-code generation."""

    def __init__(self, src=None, xml=None):
        self.attr = {}
        self.param = []
        if src is not None:
            self.from_src(src)
        elif xml is not None:
            self.from_xml(xml)

    def __repr__(self):
        return ET.tostring(self.to_xml(), encoding='unicode')

    # --- Icon ---

    def get_icon(self):
        """Return the icon filename for this feature."""
        return self.attr.get("icon", "")

    def get_version(self):
        return _get_float(self.attr.get("version", "0.0"))

    # --- Value accessors ---

    def get_value(self):
        return self.attr.get("value", "")

    def get_display_string(self):
        return self.get_value()

    def set_value(self, new_val):
        self.attr["value"] = new_val

    def get_type(self):
        return self.attr.get("type", "string")

    def get_tooltip(self):
        s = self.attr.get("tool_tip", self.attr.get("help", ""))
        return s.replace('&#176;', '\u00b0') if s else ""

    def get_attr(self, attr):
        return self.attr.get(attr, None)

    def get_param(self, param_id):
        """Find a parameter by its call name."""
        for p in self.param:
            if p.get_call() == "#%s" % param_id:
                return p
        return None

    def get_name(self):
        return self.attr.get("name", "unnamed")

    def get_grayed(self):
        return self.attr.get("grayed") == '1'

    # --- Indent ---

    def getindent(self):
        count = _get_int(self.attr.get('indent', '0'))
        return '\t' * count

    # --- Hidden fields ---

    def hide_field(self):
        if 'hidden_count' not in self.attr:
            self.attr['hidden_count'] = '1'
        else:
            self.attr['hidden_count'] = str(_get_int(self.attr['hidden_count']) + 1)

    def show_all_fields(self):
        result = 0
        for p in self.param:
            result += p.set_hidden(False)
        self.attr['hidden_count'] = '0'
        return result > 0

    def has_hidden_fields(self):
        if 'hidden_count' in self.attr:
            return _get_int(self.attr['hidden_count']) > 0
        return False

    # --- ID management ---

    def get_id(self, xml_parent=None):
        """Assign a unique ID based on existing features in project."""
        num = 1
        if xml_parent is not None:
            l = xml_parent.findall(".//feature[@type='%s']" % self.attr["type"])
            ids = [_get_int(i.get("id", "0")[-3:]) for i in l] + [0]
            num = max(ids) + 1
        self.attr["id"] = self.attr["type"] + "_%03d" % num

    # --- CFG file loading ---

    def from_src(self, src):
        """Load feature from a .cfg file."""
        # Read and strip translation markers _(" and ")
        with open(src, 'r', encoding='utf-8') as f:
            raw = f.read()

        raw = re.sub(r"_\(([\"'])", r"\1", raw)
        raw = re.sub(r"([\"'])\)", r"\1", raw)

        # Add "." prefix to preserve indentation
        raw = re.sub(r"(?m)^(\ |\t)", r"\1.", raw)

        # Use a custom parser that tolerates duplicate options (like Python 2)
        conf = {}
        current_section = None
        for line in raw.split('\n'):
            line = line.strip()
            if not line or line.startswith(';') or line.startswith('#'):
                continue
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                conf[current_section] = {}
                continue
            if current_section and '=' in line:
                key, _, value = line.partition('=')
                key = key.strip()
                value = value.strip()
                # Restore leading dot-stripped content properly
                # Only process multiline content at the end
                conf[current_section][key] = value

        # Now read with ConfigParser to get proper multiline handling
        src_config = configparser.ConfigParser(strict=False)
        try:
            src_config.read_string(raw)
            # Overlay ConfigParser values (better multiline support)
            for section in src_config.sections():
                if section not in conf:
                    conf[section] = {}
                for item in src_config.options(section):
                    s = src_config.get(section, item, raw=True)
                    s = re.sub(r"(?m)^\.", "", " " + s)[1:]
                    conf[section][item] = s
        except configparser.DuplicateOptionError:
            # Already handled by our manual parser
            pass

        self.attr = conf.get("SUBROUTINE", {})

        ftype = self.attr.get("type")
        if ftype is None:
            raise Exception("Type not defined for %s" % src)

        # Parse order
        if "order" not in self.attr:
            self.attr["order"] = []
        else:
            self.attr["order"] = self.attr["order"].upper().split()

        # Ensure PARAM_ prefix
        self.attr["order"] = [
            s if s[:6] == "PARAM_" else "PARAM_" + s
            for s in self.attr["order"]
        ]

        self.attr['hidden_count'] = '0'

        # Parse parameters
        self.param = []
        parameters = self.attr["order"] + [
            p for p in conf
            if p[:6] == "PARAM_" and p not in self.attr["order"]
        ]
        for s in parameters:
            if s in conf:
                pn = s.lower()
                p = Parameter(ini=conf[s], ini_id=pn)
                self.param.append(p)

        self.attr["id"] = ftype + '_000'

        # Load G-code sections
        for section in ["DEFINITIONS", "BEFORE", "CALL", "AFTER",
                        "VALIDATION", "INIT"]:
            if section in conf and "content" in conf[section]:
                self.attr[section.lower()] = re.sub(
                    r"(?m)\r?\n\r?\.", "\n", conf[section]["content"]
                )
            else:
                self.attr[section.lower()] = ""

        # Execute init
        parent = self
        try:
            exec(self.attr.get('init', ''))
        except Exception as e:
            print("Error in init for %s: %s" % (self.get_name(), e))

    # --- XML loading ---

    def from_xml(self, xml):
        """Load feature from XML element."""
        self.attr = {}
        for key in xml.keys():
            self.attr[key] = xml.get(key)

        self.param = []
        for p in xml:
            self.param.append(Parameter(xml=p))

    def to_xml(self):
        """Serialize to XML."""
        xml = ET.Element("feature")
        for key in self.attr:
            xml.set(key, str(self.attr[key]))

        for p in self.param:
            xml.append(p.to_xml())
        return xml

    # --- Include helpers ---

    def include(self, src):
        """Include a library file's content."""
        full_path = search_path(True, src, LIB_DIR)
        if full_path:
            with open(full_path, 'r', encoding='utf-8') as f:
                return f.read()
        return ''

    def include_once(self, src):
        """Include a library file's content (only once per session)."""
        global INCLUDE
        if src not in INCLUDE:
            INCLUDE.add(src)
            return self.include(src)
        return ""

    # --- Parameter substitution ---

    def replace_params(self, s):
        """Replace #param_xxx references with actual values."""
        for p in self.param:
            if "call" in p.attr and "value" in p.attr:
                if p.attr['type'] == 'text':
                    note_lines = p.get_value().split('\n')
                    lines = ''
                    for line in note_lines:
                        lines += '( ' + line + ' )\n'
                    s = re.sub(
                        r"%s([^A-Za-z0-9_]|$)" % re.escape(p.attr["call"]),
                        r"%s\1" % lines, s
                    )
                elif p.attr['type'] == 'gc-lines':
                    note_lines = p.get_value().split('\n')
                    lines = '\n'
                    for line in note_lines:
                        lines += '\t' + line + '\n'
                    s = re.sub(
                        r"%s([^A-Za-z0-9_]|$)" % re.escape(p.attr["call"]),
                        r"%s\1" % lines, s
                    )
                else:
                    s = re.sub(
                        r"%s([^A-Za-z0-9_]|$)" % re.escape(p.attr["call"]),
                        r"%s\1" % p.get_ngc_value(), s
                    )
        return s

    # --- G-code processing ---

    def process(self, s, line_leader=''):
        """Process G-code template with <eval>, <exec>, <subprocess>, <import>."""

        def eval_callback(m):
            try:
                return str(eval(m.group(2), {"self": self}))
            except Exception:
                return ''

        def exec_callback(m):
            text = m.group(2)
            text = text.replace("\t", " ")
            i = 1e10
            for line in reversed(text.split("\n")):
                line = line.strip()
                if line:
                    stripped = line.lstrip()
                    if text.find(line) - text.find(stripped) < i:
                        i = text.find(stripped) - text.find(line)
            if i < 1e10:
                res = ""
                for line in text.split("\n"):
                    res += line[i:] + "\n"
                text = res

            old_stdout = sys.stdout
            buf = io.StringIO()
            sys.stdout = buf
            try:
                exec(text, {"self": self})
            except Exception as e:
                print("# exec error: %s" % e, file=old_stdout)
            sys.stdout = old_stdout
            return buf.getvalue()

        def subprocess_callback(m):
            text = m.group(2)
            text = text.replace("\t", "  ")
            i = 1e10
            for line in reversed(text.split("\n")):
                line = line.strip()
                if line:
                    stripped = line.lstrip()
                    if text.find(line) - text.find(stripped) < i:
                        i = text.find(stripped) - text.find(line)
            if i < 1e10:
                res = ""
                for line in text.split("\n"):
                    res += line[i:] + "\n"
                text = res
            try:
                return subprocess.check_output(
                    [text], shell=True,
                    stderr=subprocess.STDOUT
                ).decode('utf-8', errors='replace')
            except subprocess.CalledProcessError as e:
                msg = ("Error with subprocess: returncode = %d\n"
                       "output = %s\ne= %s\n") % (
                    e.returncode, e.output.decode('utf-8', errors='replace'), e
                )
                print(msg)
                return ''

        def import_callback(m):
            fname = m.group(2)
            full_path = search_path(True, fname, PROJECTS_DIR)
            if full_path:
                with open(full_path, 'r', encoding='utf-8') as f:
                    return f.read()
            return ''

        if not s:
            return ''

        # First pass: replace parameter references
        s = self.replace_params(s)

        # Substitute special variables
        s = re.sub(r"#sub_name", self.attr.get('name', ''), s)
        s = re.sub(r"%SYS_DIR%", SYS_DIR or '', s)
        f_id = self.get_attr("id") or ''
        s = re.sub(r"#self_id", f_id, s)

        # Process template directives
        s = re.sub(r"(?i)(<import>(.*?)</import>)", import_callback, s)
        s = re.sub(r"(?i)(<eval>(.*?)</eval>)", eval_callback, s)
        s = re.sub(r"(?ims)(<exec>(.*?)</exec>)", exec_callback, s)
        s = re.sub(r"(?ims)(<subprocess>(.*?)</subprocess>)",
                   subprocess_callback, s)

        if "#ID" in s:
            if 'short_id' not in self.attr:
                self.attr['short_id'] = get_short_id()
            s = re.sub(r"#ID", self.attr['short_id'], s)

        s = s.lstrip('\n').rstrip('\n\t')
        if s == '':
            return ''

        if line_leader:
            result_s = '\n'
            for line in s.split('\n'):
                result_s += line_leader + line + '\n'
            return result_s + '\n'
        else:
            return '\n' + s + '\n\n'

    # --- G-code sections ---

    def get_definitions(self):
        s = self.attr.get("definitions", '')
        if s:
            s = self.process(s)
        return s

    # --- Validation helpers ---

    def check_hash(self, s, default=0):
        """Evaluate a hash-bracketed expression like [1+2]."""
        try:
            return 0 + eval(s.strip('[]'))
        except Exception:
            print("%s : can not evaluate %s" % (self.get_name(), s))
            return default

    def validate(self):
        """Run validation code."""
        s = self.attr.get("validation", "")
        if not s:
            return True
        s = self.replace_params(s)
        s = re.sub(r"#", r"""#""", s)
        try:
            exec(s)
        except Exception:
            print('%s failed validation' % self.get_name())
        return True

    def msg_inv(self, msg, msgid):
        """Display an info/warning message (no-op in headless mode)."""
        msg = msg.replace('&#176;', '\u00b0')
        print('%s : %s' % (self.get_name(), msg))
