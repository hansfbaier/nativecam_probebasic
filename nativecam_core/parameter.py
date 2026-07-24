"""
Parameter — holds a single parameter for a CAM feature.

Ported from NativeCAM ncam.py Parameter class (lines 1397-1586).
"""

import decimal
import locale
import re
import xml.etree.ElementTree as ET

from .preferences import DEFAULT_METRIC, DEFAULT_DIGITS

# Supported data types for parameters
SUPPORTED_DATA_TYPES = [
    'sub-header', 'header', 'bool', 'boolean', 'int', 'gc-lines',
    'tool', 'gcode', 'text', 'list', 'float', 'string', 'engrave',
    'combo', 'combo-user', 'items', 'filename', 'prjname',
]

NUMBER_TYPES = ['float', 'int']
NO_ICON_TYPES = ['sub-header', 'header']

# Global locale decimal point
try:
    locale.setlocale(locale.LC_ALL, '')
except Exception:
    pass
DECIMAL_POINT = locale.localeconv().get("decimal_point", ".")


def _get_float(s):
    """Convert string to float, handling locale."""
    try:
        return float(s)
    except (ValueError, TypeError):
        try:
            return locale.atof(s)
        except (ValueError, TypeError):
            return 0.0


def _get_int(s):
    """Convert string to int, stripping decimals."""
    try:
        idx = s.find('.')
        if idx > -1:
            s = s[:idx]
        return int(s)
    except (ValueError, TypeError):
        return 0


def _get_string(float_val, digits, localized=True):
    """Format a float to string with given precision."""
    fmt = '%' + '0.%sf' % digits
    if localized:
        try:
            return locale.format_string(fmt, float_val)
        except Exception:
            return fmt % float_val
    else:
        return fmt % float_val


class Parameter:
    """A single parameter within a CAM feature."""

    def __init__(self, ini=None, ini_id=None, xml=None):
        self.attr = {}
        if ini is not None:
            self.from_ini(ini, ini_id)
        elif xml is not None:
            self.from_xml(xml)

    def from_ini(self, ini, ini_id):
        """Load parameter from INI section dict."""
        self.attr = dict(ini)
        if "type" not in self.attr or self.attr["type"] not in SUPPORTED_DATA_TYPES:
            self.attr["type"] = 'string'

        if "call" not in self.attr:
            self.attr["call"] = "#" + ini_id

    def from_xml(self, xml):
        """Load parameter from XML element."""
        for key in xml.keys():
            self.attr[key] = xml.get(key)

    def to_xml(self):
        """Serialize parameter to XML element."""
        xml = ET.Element("param")
        for key in self.attr:
            xml.set(key, str(self.attr[key]))
        return xml

    def __repr__(self):
        return ET.tostring(self.to_xml(), encoding='unicode')

    # --- Value accessors ---

    def get_value(self, editor=False):
        """Get display value (metric-converted if applicable)."""
        if self.get_type() == 'float':
            if DEFAULT_METRIC and "metric_value" in self.attr:
                return _get_string(_get_float(self.attr["value"]) * 25.4, 6, editor)
            else:
                return _get_string(_get_float(self.attr["value"]), 6, editor)
        else:
            return self.attr.get("value", "")

    def get_ngc_value(self):
        """Get the value for NGC (G-code) output (machine units)."""
        from .preferences import MACHINE_METRIC
        if self.get_type() == 'gcode':
            val = self.attr.get("value", "")
            return val if val != '' else '0'
        if self.get_type() == 'float':
            if MACHINE_METRIC and "metric_value" in self.attr:
                return _get_string(_get_float(self.attr["value"]) * 25.4, 6, False)
            else:
                return _get_string(_get_float(self.attr["value"]), 6, False)
        else:
            return self.attr.get("value", "")

    def get_display_string(self):
        """Get human-readable display string."""
        if self.get_type() == "float":
            if DEFAULT_METRIC and "metric_value" in self.attr:
                return _get_string(_get_float(self.attr["value"]) * 25.4, self.get_digits())
            else:
                return _get_string(_get_float(self.attr["value"]), self.get_digits())
        else:
            return self.attr.get("value", "")

    def set_value(self, new_val, parent=None):
        """Set parameter value, handling metric conversion and type changes."""
        done = False
        cancel = False
        if 'on_change' in self.attr:
            exec(self.attr['on_change'])
        if cancel:
            return False
        if not done:
            if self.get_type() == "float":
                factor = 25.4 if (DEFAULT_METRIC and "metric_value" in self.attr) else 1
                new_val = _get_string(_get_float(new_val) / factor, 10, False)
                old_val = _get_string(_get_float(self.attr["value"]), 10, False)
            else:
                old_val = self.attr["value"]
            if new_val == old_val:
                return False
            else:
                self.attr["value"] = new_val
        if 'value_changed' in self.attr:
            exec(self.attr['value_changed'])
        return True

    # --- Type accessors ---

    def get_type(self):
        return self.attr.get("type", "string")

    def set_type(self, new_type):
        self.attr['old_type'] = self.attr['type']
        self.attr['type'] = new_type
        if new_type == 'gcode' and DEFAULT_METRIC and "metric_value" in self.attr:
            self.attr["value"] = self.attr["metric_value"]

    def revert_type(self):
        if 'old_type' in self.attr:
            if self.attr['old_type'] == 'float':
                val = _get_float(self.attr['value'])
                min_v = _get_float(self.get_min_value())
                max_v = _get_float(self.get_max_value())
                if val < min_v:
                    val = min_v
                if val > max_v:
                    val = max_v
                self.attr['value'] = str(val)
                self.attr['type'] = 'float'
            elif self.attr['old_type'] == 'int':
                val = _get_int(self.attr['value'])
                min_v = _get_int(self.get_min_value())
                max_v = _get_int(self.get_max_value())
                if val < min_v:
                    val = min_v
                if val > max_v:
                    val = max_v
                self.attr['value'] = str(val)
                self.attr['type'] = 'int'

    # --- Attribute accessors ---

    def get_attr(self, name):
        return self.attr.get(name, None)

    def get_name(self):
        return self.attr.get("name", "")

    def get_options(self):
        return self.attr.get("options", "")

    def get_tooltip(self):
        return self.attr.get("tool_tip", self.get_name())

    def get_digits(self):
        if self.get_type() == 'int':
            return 0
        else:
            digits = self.attr.get("digits", DEFAULT_DIGITS)
            return int(digits) if digits else DEFAULT_DIGITS

    def set_digits(self, new_digits):
        self.attr["digits"] = str(new_digits)

    def get_min_value(self):
        min_v = self.attr.get("minimum_value", "-999999.9")
        if self.get_type() == 'float' and DEFAULT_METRIC and 'metric_value' in self.attr:
            return str(_get_float(min_v) * 25.4)
        return min_v

    def get_max_value(self):
        max_v = self.attr.get("maximum_value", "999999.9")
        if self.get_type() == 'float' and DEFAULT_METRIC and 'metric_value' in self.attr:
            return str(_get_float(max_v) * 25.4)
        return max_v

    # --- Visibility ---

    def get_hidden(self):
        return 'hidden' in self.attr and self.attr['hidden'] == '2'

    def set_hidden(self, hide):
        if hide:
            self.attr['hidden'] = '2'
        elif self.get_hidden():
            self.attr['hidden'] = '0'
            return 1
        return 0

    def get_grayed(self):
        return self.attr.get("grayed") == '1'

    def set_grayed(self, value):
        self.attr["grayed"] = '1' if value else '0'

    # --- Groups ---

    def change_group(self):
        t = self.get_type()
        if t in ['sub-header', 'header']:
            if t == 'sub-header':
                if 'header' in self.attr:
                    return False
                self.set_type('header')
            else:
                self.set_type('sub-header')
            return True
        return False

    def get_header(self):
        return self.attr.get("header", "")

    def get_call(self):
        return self.attr.get("call", "")
