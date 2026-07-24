#!/usr/bin/env python3
"""Generate markdown documentation for all NativeCAM operations from .cfg files."""

import sys, os, re, json

sys.path.insert(0, os.path.dirname(__file__))
import nativecam_core.feature as feat
feat.NCAM_DIR = os.path.join(os.path.dirname(__file__), '..', 'NativeCAM')
feat.SYS_DIR = feat.NCAM_DIR

from nativecam_core.feature import Feature, search_path
from nativecam_core.menu_loader import MenuLoader

DOC_DIR = os.path.join(os.path.dirname(__file__), 'doc')

TYPE_LABELS = {
    'bool': 'Toggle', 'float': 'Float', 'int': 'Integer',
    'combo': 'Dropdown', 'combo-user': 'Dropdown (editable)',
    'gcode': 'G-code', 'text': 'Text', 'list': 'List',
    'header': '— HEADER —', 'sub-header': '— Sub-header —',
}

def slug(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

def build_catalog(catalog):
    ml = MenuLoader()
    ml.load(catalog, ncam_dir=feat.NCAM_DIR)
    items = ml.get_menu_hierarchy()
    base = os.path.join(DOC_DIR, catalog)
    os.makedirs(base, exist_ok=True)
    return base, items

def write_feature_doc(base_path, entry):
    src = entry.get('src')
    if not src:
        return

    cfg_path = search_path(False, src)
    if not cfg_path:
        print(f"  SKIP {entry['name']}: cfg not found at {src}")
        return

    try:
        f = Feature(src=cfg_path)
    except Exception as e:
        print(f"  SKIP {entry['name']}: parse error: {e}")
        return

    name = f.get_name()
    ftype = f.get_type()
    tooltip = f.get_tooltip()
    icon = f.get_icon()

    lines = []
    lines.append(f"# {name}")
    lines.append("")
    if tooltip:
        lines.append(f">{tooltip}")
        lines.append("")

    lines.append("| | |")
    lines.append("|---|---|")
    lines.append(f"| Type | `{ftype}` |")
    if icon:
        lines.append(f"| Icon | `{icon}` |")
    lines.append(f"| Source | `{src}` |")
    lines.append("")

    # Subroutine info
    lines.append("## Subroutine")
    lines.append("")
    sub_call = f.attr.get('ngc', f.attr.get('call', f"`{ftype}.ngc`"))
    lines.append(f"- **NGC**: `{sub_call}`")
    sub = f.attr.get('sub')
    if sub:
        lines.append(f"- **Sub number**: `{sub}`")
    lines.append("")

    # Parameters
    lines.append("## Parameters")
    lines.append("")
    lines.append("| # | Parameter | Type | Default |")
    lines.append("|---|-----------|------|---------|")

    for i, p in enumerate(f.param):
        p_type = p.get_type()
        p_name = p.get_name()
        p_call = p.get_call()
        p_val = p.get_display_string()
        p_tip = p.get_tooltip()

        type_label = TYPE_LABELS.get(p_type, p_type)
        val_display = p_val if p_val else ''

        if p_type in ('header', 'sub-header'):
            lines.append(f"| | **{p_name}** | | |")
        else:
            lines.append(f"| {i+1} | {p_name} | {type_label} | `{val_display}` |")

    lines.append("")

    # Detailed param info
    lines.append("## Parameter Details")
    lines.append("")
    for p in f.param:
        p_type = p.get_type()
        if p_type in ('header', 'sub-header'):
            continue
        p_name = p.get_name()
        p_call = p.get_call()
        p_tip = p.get_tooltip()
        lines.append(f"### {p_name}")
        lines.append(f"- **NGC variable**: `{p_call}`")
        if p_tip:
            lines.append(f"- {p_tip}")
        if p_type == 'float':
            lines.append(f"- **Min**: {p.get_min_value()}  **Max**: {p.get_max_value()}  **Digits**: {p.get_digits()}")
        if p_type in ('combo', 'combo-user', 'list'):
            opts = p.get_options()
            if opts:
                lines.append(f"- **Options**: {opts}")
        lines.append("")

    # G-code sections
    sections = [
        ('before', 'Before (preamble)'),
        ('call', 'Call (main subroutine)'),
        ('after', 'After (postamble)'),
        ('definitions', 'Definitions'),
    ]
    has_any = any(f.attr.get(s[0], '') for s in sections)
    if has_any:
        lines.append("## G-code Template")
        lines.append("")
        for key, label in sections:
            content = f.attr.get(key, '')
            if content:
                lines.append(f"### {label}")
                lines.append("")
                lines.append("```ngc")
                lines.append(content.strip())
                lines.append("```")
                lines.append("")

    doc = '\n'.join(lines)
    fname = slug(name) + '.md'
    path = os.path.join(base_path, fname)
    with open(path, 'w') as fh:
        fh.write(doc)
    return name, fname

def walk_menu(base_path, items, prefix=""):
    """Walk menu hierarchy and generate docs."""
    results = []
    for entry in items:
        name = entry['name']
        if entry['is_menu']:
            results.append(('menu', name, ''))
            results.extend(walk_menu(base_path, entry['children'], name + ' > '))
        elif entry.get('src'):
            result = write_feature_doc(base_path, entry)
            if result:
                results.append(('feature', result[0], result[1]))
    return results

def write_index(base_path, catalog, results):
    """Write index.md for a catalog."""
    lines = []
    title = catalog.capitalize()
    lines.append(f"# {title} Operations")
    lines.append("")
    lines.append(f"Auto-generated documentation for all {title} CAM operations.")
    lines.append("")

    current_menu = None
    for kind, name, filename in results:
        if kind == 'menu':
            current_menu = name
            lines.append(f"## {name}")
            lines.append("")
        elif kind == 'feature':
            if current_menu:
                lines.append(f"- [{name}]({filename}) — `{current_menu} > {name}`")
            else:
                lines.append(f"- [{name}]({filename})")

    with open(os.path.join(base_path, 'index.md'), 'w') as fh:
        fh.write('\n'.join(lines))

# ── Main ──────────────────────────────────────────────────────────

catalogs = ['mill', 'lathe', 'plasma']
for catalog in catalogs:
    print(f"\n=== {catalog.upper()} ===")
    base, items = build_catalog(catalog)
    results = walk_menu(base, items)
    write_index(base, catalog, results)
    features = [r for r in results if r[0] == 'feature']
    print(f"  Generated {len(features)} feature docs + index.md")

print(f"\nAll docs written to {DOC_DIR}/")
