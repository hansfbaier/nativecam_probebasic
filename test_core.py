#!/usr/bin/env python3
"""Standalone test runner for nativecam_core — no Qt or LinuxCNC needed.

Usage:  cd /home/jack/CNC/probebasic && python3 nativecam/test_core.py
"""

import sys
import os

# Add nativecam to path
_NATIVE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _NATIVE_DIR)

import nativecam_core.feature as feat
feat.NCAM_DIR = _NATIVE_DIR
feat.SYS_DIR = _NATIVE_DIR

from nativecam_core.feature import Feature, search_path
from nativecam_core.menu_loader import MenuLoader
from nativecam_core.gcode_generator import GCodeGenerator
import xml.etree.ElementTree as ET

passed = 0
failed = 0

def check(label, condition, detail=""):
    global passed, failed
    if condition:
        passed += 1
        print(f"  PASS  {label}")
    else:
        failed += 1
        print(f"  FAIL  {label}  {detail}")

# ── Test 1: Feature loading ──────────────────────────────────────
print("=== Test 1: Feature loading ===")
f = Feature(src=os.path.join(feat.NCAM_DIR, 'cfg/mill/circle.cfg'))
check("type is 'circle'",              f.get_type() == 'circle')
check("name contains 'Circle'",         'Circle' in f.get_name())
check("has 24 params",                 len(f.param) == 24)
check("param #param_act is bool",      f.param[0].get_type() == 'bool')
p_d = f.get_param("param_d")
check("param #param_d exists",         p_d is not None)
check("param #param_d has metric_val", p_d is not None and p_d.attr.get('metric_value') is not None)

# ── Test 2: Menu loading ─────────────────────────────────────────
print("\n=== Test 2: Menu loading ===")
ml = MenuLoader()
items = ml.load('mill')
features = [i for i in items if i.src]
check("loads 70+ menu items",          len(items) >= 70, f"got {len(items)}")
check("has 49 mill features",          len(features) == 49, f"got {len(features)}")
check("contains 'Basic Shapes'",        any('Basic Shapes' in i.name for i in items))
hierarchy = ml.get_menu_hierarchy()
check("menu hierarchy has entries",    len(hierarchy) > 0)

# ── Test 3: All features parse ───────────────────────────────────
print("\n=== Test 3: All 49 features parse ===")
parse_fails = []
for fi in features:
    try:
        cfg_path = search_path(False, fi.src)
        if cfg_path is None:
            parse_fails.append(f"{fi.name}: file not found")
            continue
        Feature(src=cfg_path)
    except Exception as e:
        parse_fails.append(f"{fi.name}: {e}")
check("all 49 parse", len(parse_fails) == 0,
      f"{len(parse_fails)} failures: {'; '.join(parse_fails[:3])}")

# ── Test 4: G-code generation ────────────────────────────────────
print("\n=== Test 4: Single-feature G-code ===")
f = Feature(src=os.path.join(feat.NCAM_DIR, 'cfg/mill/rectangle.cfg'))
xml = ET.Element('lcnc-ncam')
f.get_id(xml)
xml.append(f.to_xml())
gcode = GCodeGenerator().generate(xml)
check("generates rectangle G-code",    'o<rectangle' in gcode)
check("> 500 chars",                   len(gcode) > 500, f"got {len(gcode)}")
check("has metric conversion",         '50.800000' in gcode)

# ── Test 5: Multi-feature G-code ─────────────────────────────────
print("\n=== Test 5: Multi-feature G-code ===")
xml = ET.Element('lcnc-ncam')
for src in ['cfg/mill/circle.cfg', 'cfg/mill/rectangle.cfg',
            'cfg/mill/drill-single.cfg', 'cfg/mill/slot.cfg',
            'cfg/mill/polygon.cfg']:
    fp = os.path.join(feat.NCAM_DIR, src)
    f = Feature(src=fp)
    f.get_id(xml)
    xml.append(f.to_xml())
gcode = GCodeGenerator().generate(xml)
check("contains circle",               'o<circle' in gcode)
check("contains rectangle",            'o<rect' in gcode)
check("contains drill",                'o<drill' in gcode)
check("> 2000 chars",                  len(gcode) > 2000, f"got {len(gcode)}")

# ── Test 6: Feature XML round-trip ───────────────────────────────
print("\n=== Test 6: XML round-trip ===")
f = Feature(src=os.path.join(feat.NCAM_DIR, 'cfg/mill/circle.cfg'))
xml1 = f.to_xml()
f2 = Feature(xml=xml1)
xml2 = f2.to_xml()
check("round-trip preserves type",     f.get_type() == f2.get_type())
check("round-trip preserves name",     f.get_name() == f2.get_name())
check("round-trip preserves params",   len(f.param) == len(f2.param))

# ── Test 7: Parameter value access ───────────────────────────────
print("\n=== Test 7: Parameter values ===")
f = Feature(src=os.path.join(feat.NCAM_DIR, 'cfg/mill/drill-single.cfg'))
px = f.get_param("param_x")
py = f.get_param("param_y")
check("X param exists",                px is not None)
check("Y param exists",                py is not None)
if px:
    check("X default is 0",            px.get_ngc_value() in ('0', '0.000000'))
    px.attr['value'] = '1.5'
    # ngc_value does metric conversion: 1.5 in → 38.1 mm
    check("X set to 1.5 (raw)",        px.attr['value'] == '1.5')
    check("X ngc_value is 38.1",       px.get_ngc_value() == '38.100000')
    check("X is float type",           px.get_type() == 'float')

# ── Summary ──────────────────────────────────────────────────────
total = passed + failed
print(f"\n{'='*60}")
print(f"Results: {passed}/{total} passed, {failed} failed")
exit(0 if failed == 0 else 1)
