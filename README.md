# NativeCAM for Probe Basic

A Qt5/PyQt5 port of [NativeCAM](https://github.com/FernV/NativeCAM) running as a
user tab in [Probe Basic](https://github.com/kcjengr/probe_basic).

NativeCAM is a real-time conversational CAM tool for LinuxCNC. It reads
parameterized feature definitions (`.cfg` files) for milling, lathe, and
plasma operations and generates valid NGC G-code from them through a tree-based
project interface.

The original NativeCAM used GTK2/Python 2. This port extracts the data model
(`nativecam_core`) and rebuilds the UI as a PyQt5 user tab widget compatible
with qtpyvcp and Probe Basic.

## Features

- **49 mill features** — rectangles, circles, slots, ellipses, polygons,
  drilling patterns, counterbores, thread milling, probing macros, and more
- **Dynamic parameter editor** — spin boxes, checkboxes, combos, and text
  fields generated from the `.cfg` definitions
- **G-code generation** — validated, metric/imperial-converted output with
  subroutine calls to the original NGC libraries
- **Undo/redo, duplicate, drag-reorder** — standard project-tree operations
- **Build + auto-refresh** — generate G-code and optionally load it into
  LinuxCNC automatically
- **Catalog switching** — Mill, Lathe, and Plasma catalogs

## Directory structure

```
probebasic/
├── NativeCAM/                    # Original NativeCAM (cfg, lib, graphics)
├── nativecam/                    # Ported user tab (this project)
│   ├── nativecam.py              # UserTab QWidget
│   ├── nativecam.ui              # Qt Designer layout
│   └── nativecam_core/           # Extracted data model
│       ├── parameter.py          # Parameter class
│       ├── feature.py            # Feature: cfg loader, G-code templates
│       ├── menu_loader.py        # Catalog menu.xml parser
│       ├── gcode_generator.py    # Tree → G-code compiler
│       └── preferences.py        # Metric/imperial, config
├── probe_basic/
│   └── configs/
│       ├── probe_basic/
│       │   └── user_tabs/
│       │       └── nativecam → ../../../nativecam  (symlink)
│       └── probe_basic_lathe/
│           └── user_tabs/
│               └── nativecam → ../../../nativecam  (symlink)
└── qtpyvcp/
```

## Installation

1. Ensure Probe Basic and qtpyvcp are installed (see
   `probe_basic/install_for_qtpyvcp.sh`).

2. The `nativecam/` directory is already symlinked into both mill and lathe
   config `user_tabs/` directories.

3. Enable user tabs in your `probe_basic.ini`:

   ```ini
   [DISPLAY]
   USER_TABS_PATH = user_tabs/
   ```

4. Add the NativeCAM subroutine libraries to LinuxCNC's search path
   (in your `.ini` or through the `SUBROUTINE_PATH` setting):

   ```ini
   [RS274NGC]
   SUBROUTINE_PATH = subroutines:NativeCAM/lib/mill:NativeCAM/lib/utilities:NativeCAM/my-stuff
   ```

5. Launch Probe Basic:

   ```bash
   cd probe_basic/configs/probe_basic
   ./launch_probe_basic.sh
   ```

   The NativeCAM tab will appear alongside the other main tabs.

## Development

The core library is pure Python 3 with no Qt dependencies. You can test it
standalone:

```bash
cd /home/jack/CNC/probebasic
python3 -c "
import sys
sys.path.insert(0, 'nativecam')
import nativecam_core.feature as feat
feat.NCAM_DIR = 'NativeCAM'
feat.SYS_DIR = 'NativeCAM'

from nativecam_core.feature import Feature
f = Feature(src='NativeCAM/cfg/mill/circle.cfg')
print(f.get_name(), f.get_type(), len(f.param), 'params')
"
```

To recompile Qt resources after changes:

```bash
cd probe_basic && qcompile .
```

## Known limitations

- **ttt.py** (TrueType engraving) has been ported to Python 3 and is included
  in `NativeCAM/ttt`, but requires the `truetype-tracer` system tool.
- The parameter editor does not yet support inline editing in the project tree
  (the original GTK2 version used a `CellRenderer` for this).
- Sub-header grouping and linked combo-user parameters are partially supported.

## License

Copyright © 2017 Fernand Veilleux, Nick Drobchenko, and contributors.

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc., 51 Franklin
Street, Fifth Floor, Boston, MA 02110-1301 USA.
