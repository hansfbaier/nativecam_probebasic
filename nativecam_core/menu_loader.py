"""
MenuLoader — parse NativeCAM catalog menu.xml files.

Ported from NativeCAM ncam.py catalog loading logic.
"""

import os
import re
import xml.etree.ElementTree as ET

from .feature import search_path, CATALOGS_DIR


class MenuItem:
    """A single item in the catalog menu."""

    def __init__(self, element):
        self.action = element.get("action", "")
        self.name = element.get("name", self.action)
        self.tool_tip = element.get("tool_tip", "")
        self.src = element.get("src", "")      # Path to .cfg file
        self.icon = element.get("icon", "")
        self.tag = element.tag      # "menu" or "menuitem"

    def is_menu(self):
        return self.tag == "menu"


class MenuLoader:
    """Loads and parses NativeCAM catalog menus."""

    def __init__(self):
        self.catalog = "mill"
        self.items = []  # Flat list of all menu items
        self.menu_tree = None  # Root XML element

    def load(self, catalog="mill", ncam_dir=None):
        """Load the menu for a given catalog."""
        self.catalog = catalog
        self.items = []

        # Set NCAM_DIR for search
        if ncam_dir:
            import nativecam_core.feature as feat
            feat.NCAM_DIR = ncam_dir

        # Try custom menu first, then default
        catname = self.catalog + '/menu-custom.xml'
        cat_path = search_path(None, catname, CATALOGS_DIR)
        if cat_path is None:
            catname = self.catalog + '/menu.xml'
            cat_path = search_path(True, catname, CATALOGS_DIR)

        if cat_path is None:
            raise FileNotFoundError(
                "No menu found for catalog '%s'" % catalog
            )

        with open(cat_path, 'r', encoding='utf-8') as f:
            menu_xml = f.read()

        # Strip GTK translation markers — handle both double and single quotes
        menu_xml = re.sub(r"_\(([\"'])", r"\1", menu_xml)
        menu_xml = re.sub(r"([\"'])\)_", r"\1", menu_xml)

        self.menu_tree = ET.fromstring(menu_xml)
        self._parse_menu(self.menu_tree)
        return self.items

    def _parse_menu(self, element, parent_path=""):
        """Recursively parse menu/submenu items."""
        for child in element:
            item = MenuItem(child)
            if parent_path:
                item.name = parent_path + " > " + item.name
            self.items.append(item)

            if item.is_menu():
                self._parse_menu(child, item.name)

    def get_items_by_src(self):
        """Build a dict mapping src path to menu item."""
        result = {}
        for item in self.items:
            if item.src:
                result[item.src] = item
        return result

    def get_menu_hierarchy(self, element=None):
        """Build a hierarchical tree structure for UI rendering."""
        if element is None:
            element = self.menu_tree

        result = []
        for child in element:
            item = MenuItem(child)
            entry = {
                'action': item.action,
                'name': item.name,
                'tool_tip': item.tool_tip,
                'src': item.src,
                'icon': item.icon,
                'is_menu': item.is_menu(),
                'children': [],
            }
            if item.is_menu():
                entry['children'] = self.get_menu_hierarchy(child)
            result.append(entry)
        return result

    def find_src(self, action):
        """Find the cfg src path for a given action."""
        for item in self.items:
            if item.action == action and item.src:
                return item.src
        return None

    def resolve_src_path(self, src):
        """Resolve a cfg src path to an absolute file path."""
        if not src:
            return None
        return search_path(True, src)
