# AGENTS.md — NativeCAM Probe Basic port

## What this is

A Python 3 / PyQt5 port of NativeCAM running as a user tab inside Probe Basic
(qtpyvcp). The original NativeCAM (GTK2 / Python 2) lives in the sibling
`../NativeCAM/` directory. This repo contains only the port — the UI layer
plus a standalone `nativecam_core` data-model library.

## Workspace layout

```
probebasic/                        # workspace root (NOT this repo)
├── NativeCAM/                     # original NativeCAM — cfg/, lib/, graphics/
├── nativecam/                     # ← this repo
├── probe_basic/                   # Probe Basic GUI framework
│   ├── configs/
│   │   ├── probe_basic/           # mill config
│   │   │   └── user_tabs/
│   │   │       └── nativecam → ../../../nativecam  (symlink)
│   │   └── probe_basic_lathe/     # lathe config
│   │       └── user_tabs/
│   │           └── nativecam → ../../../nativecam  (symlink)
│   └── src/                       # Probe Basic source
└── qtpyvcp/                       # qtpyvcp framework
```

The symlinks allow a single copy of this repo to serve both mill and lathe
configs. The `nativecam.py` file computes the path to `NativeCAM/` by walking
up two `dirname()` calls from `__file__` — so it expects to be placed as a
sibling of `NativeCAM/`.

## Architecture

### nativecam_core/ — pure Python 3, no Qt

| Module | Purpose |
|---|---|
| `parameter.py` | A single parameter (`bool`, `float`, `combo`, etc.) with read/write/get/set methods and metric conversion |
| `feature.py` | A CAM feature (circle, rectangle, drill…) loaded from a `.cfg` file. Owns a list of Parameters, handles G-code template processing (`<eval>`, `<exec>`, `<subprocess>`, `<import>`) and parameter substitution (`#param_xxx`) |
| `menu_loader.py` | Parses `catalogs/*/menu.xml` into a tree of menus and feature items |
| `gcode_generator.py` | Walks an XML project tree of Features and recursively generates G-code |
| `preferences.py` | Global `DEFAULT_METRIC`, `MACHINE_METRIC`, `DEFAULT_DIGITS`, icon sizes |

### nativecam.py / nativecam.ui — PyQt5 user tab

The `UserTab(QWidget)` class is loaded dynamically by probe_basic's
`load_user_tabs()` via `importlib.util.spec_from_file_location`. This means
**relative imports do not work** at the top level — we insert the directory
into `sys.path` and use absolute imports for `nativecam_core.*`.

The UI has:
- **Left panel**: Catalog tree (populated from `menu.xml`)
- **Center panel**: Project tree (user's added Features)
- **Right panel**: Dynamic parameter editor (`_build_parameter_editor`)
- **Bottom**: G-code preview text area
- **Toolbar**: Build, Export, Auto-refresh, Undo/Redo

Parameter widgets are created dynamically by `_create_param_widget()`:
`bool` → QCheckBox, `float` → QDoubleSpinBox, `int` → QSpinBox,
`combo` → QComboBox, `gcode`/`text` → QPlainTextEdit with `_FocusLostFilter`.

### Data flow

```
menu.xml → MenuLoader → catalog QTreeWidget
                              ↓ double-click
.cfg file → Feature(src=…) → project QTreeWidget + _features[]
                              ↓ selection
                        Feature.param[] → parameter editor widgets
                              ↓ Build
                        GCodeGenerator.generate() → QPlainTextEdit + file
```

## Key design decisions

1. **cfg files are not modified**. The original `.cfg` files in `NativeCAM/cfg/`
   are read at runtime from the filesystem. The port only reads them.

2. **NGC subroutine libraries are not bundled**. They live in `NativeCAM/lib/`
   and must be added to LinuxCNC's `SUBROUTINE_PATH` via the INI file.

3. **`_FocusLostFilter` inherits from `QObject`**. `QPlainTextEdit.installEventFilter()`
   requires a `QObject` argument. The filter commits edits on focus loss.

4. **Undo stack is a snapshot list**. Each undo push deep-copies the entire
   `_features` list via `Feature(xml=copy.deepcopy(f.to_xml()))`. Stack is
   capped at 200 entries.

5. **G-code preview on build, not on every param change**. Reduces overhead.

## Integration points with probe_basic

- `STATUS = getPlugin('status')` — for machine state (metric/imperial)
- `TOOL_TABLE = getPlugin('tooltable')` — available for tool selection
- `_load_into_linuxcnc()` — writes G-code to `NCAM_DIR/scripts/ncam.ngc` and
  calls `linuxcnc.command().program_open()`
- `NCAM_DIR` and `SYS_DIR` module globals in `feature.py` — set at import time
  from `nativecam.py`

## Known issues / work remaining

- **Sub-header grouping** is partially implemented. Parameters with `header=`
  should be visually grouped under their header widget, but currently use a
  simpler flat layout.
- **Linked combo-user parameters** — when a combo-user changes value, linked
  parameters should be shown/hidden. The original code handled this through
  GTK's `set_edit_datatype` callback chain; we need a PyQt5 equivalent.
- **Inline tree editing** — the original let users edit values directly in the
  project tree. Our port uses a separate right-panel editor.
- **Lathe catalog** — untested (the catalog loads, but NGC subroutines likely
  need path adjustments).
- **ttt.py** — ported to Python 3 but requires `truetype-tracer` binary.
- **Validation dialogs** — NativeCAM showed warning dialogs with checkboxes to
  suppress future warnings. Not yet ported.

## Testing standalone (no LinuxCNC needed)

```bash
cd /home/jack/CNC/probebasic
python3 -c "
import sys; sys.path.insert(0, 'nativecam')
import nativecam_core.feature as feat
feat.NCAM_DIR = 'NativeCAM'
feat.SYS_DIR = 'NativeCAM'

from nativecam_core.feature import Feature
from nativecam_core.menu_loader import MenuLoader
from nativecam_core.gcode_generator import GCodeGenerator
import xml.etree.ElementTree as ET

# Load menu
ml = MenuLoader(); ml.load('mill')
print(len([i for i in ml.items if i.src]), 'features')

# Test single feature
f = Feature(src='NativeCAM/cfg/mill/circle.cfg')
xml = ET.Element('lcnc-ncam'); xml.append(f.to_xml())
gcode = GCodeGenerator().generate(xml)
print(len(gcode), 'chars of G-code')
"
```

## Config checklist for new machines

1. Symlink `nativecam/` into `probe_basic/configs/<machine>/user_tabs/nativecam`
2. In the INI: `USER_TABS_PATH = user_tabs/` (uncommented)
3. In the INI: `SUBROUTINE_PATH` includes `NativeCAM/lib/<catalog>:NativeCAM/lib/utilities:NativeCAM/my-stuff`
