"""
NativeCAM Core — Extracted data model from NativeCAM ncam.py.

This package is a Python 3 port of the core CAM logic from NativeCAM,
stripped of all GTK2 UI code. It handles:

- .cfg file parsing (INI-based feature definitions)
- menu.xml catalog loading
- Parameter and Feature data model
- G-code generation (template processing with <eval>, <exec>, <subprocess>)
- Preferences management
- Tool table integration
- Metric/imperial conversion

Original: https://github.com/FernV/NativeCAM
License: GPLv2
"""

from .parameter import Parameter
from .feature import Feature
from .menu_loader import MenuLoader
from .gcode_generator import GCodeGenerator
from .preferences import Preferences

__version__ = '0.1.0'
