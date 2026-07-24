"""
GCodeGenerator — build G-code from a project tree of Features.

Ported from NativeCAM ncam.py to_gcode() and action_build() methods.
"""

import os
import xml.etree.ElementTree as ET

from .feature import Feature, search_path, NCAM_DIR
from .preferences import Preferences

# Global unique ID counter (shared with feature module)
from .feature import UNIQUE_ID

GENERATED_FILE = "ncam.ngc"
NGC_DIR = "scripts"


class GCodeGenerator:
    """Generates G-code from a tree of Feature objects."""

    def __init__(self, preferences=None):
        self.pref = preferences or Preferences()

    def generate(self, project_tree_xml):
        """
        Generate G-code from a project represented as an XML tree.

        Args:
            project_tree_xml: ET.Element with root tag <lcnc-ncam>

        Returns:
            str: Complete G-code program.
        """
        global UNIQUE_ID
        UNIQUE_ID = 9

        # Clear global state
        import nativecam_core.feature as feat
        feat.INCLUDE = set()
        feat.DEFINITIONS = []

        gcode = ""
        gcode_def = ""

        for child in project_tree_xml:
            g, d = self._recursive(child, '')
            gcode += g
            gcode_def += d

        if self.pref.use_pct:
            return (self.pref.default + gcode_def +
                    "(end sub definitions)\n\n" +
                    gcode + self.pref.ngc_post_amble + '\n%\n')
        else:
            return (self.pref.default + gcode_def +
                    "(end sub definitions)\n\n" +
                    gcode + self.pref.ngc_post_amble + '\nM2\n')

    def _recursive(self, xml_element, leader):
        """Recursively process an XML element and its children."""
        gcode_def = ""
        gcode = ""
        sub_leader = leader

        if xml_element.tag == "feature":
            f = Feature(xml=xml_element)
            f.validate()
            sub_leader += f.getindent()
            gcode_def += f.get_definitions()
            gcode += f.process(f.attr.get("before", ""), leader)
            gcode += f.process(f.attr.get("call", ""), leader)

        for child in xml_element:
            g, d = self._recursive(child, sub_leader + '\t')
            gcode += g
            gcode_def += d

        if xml_element.tag == "feature":
            f = Feature(xml=xml_element)
            gcode += f.process(f.attr.get("after", ""), leader)

        return gcode, gcode_def

    def generate_and_save(self, project_tree_xml, output_path=None):
        """Generate G-code and write to file."""
        if output_path is None:
            if NCAM_DIR is None:
                raise ValueError("NCAM_DIR not set")
            nc_dir = os.path.join(NCAM_DIR, NGC_DIR)
            os.makedirs(nc_dir, exist_ok=True)
            output_path = os.path.join(nc_dir, GENERATED_FILE)

        gcode = self.generate(project_tree_xml)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(gcode)

        return output_path, gcode

    def tree_to_xml(self, features):
        """
        Convert a list of Feature objects to an XML tree structure.

        This is the reverse of treestore_to_xml in NativeCAM.
        """
        xml = ET.Element("lcnc-ncam")
        for f in features:
            xml.append(f.to_xml())
        return xml
