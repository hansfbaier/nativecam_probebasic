#!/usr/bin/env python3
"""
NativeCAM — qtpyvcp user tab port.

Ported from NativeCAM ncam.py NCam class (GTK2 → PyQt5).
Provides a CAM feature tree interface for LinuxCNC G-code generation.

Usage: Place this folder in probe_basic/configs/<machine>/user_tabs/nativecam/
"""

import copy
import os
import sys
import xml.etree.ElementTree as ET

from qtpy import uic
from qtpy.QtCore import Qt, QTimer, QObject, QEvent
from qtpy.QtGui import QIcon, QFont
from qtpy.QtWidgets import (
    QWidget, QTreeWidgetItem, QHeaderView, QFileDialog,
    QMessageBox, QDoubleSpinBox, QSpinBox, QCheckBox, QComboBox,
    QLineEdit, QLabel, QTextEdit, QPlainTextEdit, QHBoxLayout,
)

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger
from qtpyvcp.utilities.info import Info

# Import core library — use sys.path since importlib loader breaks relative imports
_TAB_DIR = os.path.dirname(os.path.abspath(__file__))
if _TAB_DIR not in sys.path:
    sys.path.insert(0, _TAB_DIR)

import nativecam_core.feature as feat
from nativecam_core.feature import Feature, search_path
from nativecam_core.menu_loader import MenuLoader
from nativecam_core.gcode_generator import GCodeGenerator, GENERATED_FILE
from nativecam_core.parameter import Parameter
from nativecam_core.preferences import Preferences, DEFAULT_METRIC

LOG = logger.getLogger(__name__)

STATUS = getPlugin('status')
TOOL_TABLE = getPlugin('tooltable')
INFO = Info()

# Determine NCAM_DIR from environment or workspace
# Use realpath: importlib loader may set __file__ to a symlink path
_HERE = os.path.dirname(os.path.realpath(__file__))
# Walk up until we find NativeCAM/ (sibling of workspace root)
_feat_dir = None
_d = _HERE
for _ in range(5):
    _test = os.path.join(_d, 'NativeCAM')
    if os.path.isdir(_test):
        _feat_dir = _test
        break
    _d = os.path.dirname(_d)
if _feat_dir:
    feat.NCAM_DIR = _feat_dir
    feat.SYS_DIR = _feat_dir


class _FocusLostFilter(QObject):
    """Event filter that calls callback on FocusOut."""
    def __init__(self, callback):
        super().__init__()
        self._callback = callback

    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusOut:
            self._callback()
        return False


class UserTab(QWidget):
    """NativeCAM port as a probe_basic user tab."""

    def __init__(self, parent=None):
        super(UserTab, self).__init__(parent)
        ui_file = os.path.splitext(os.path.basename(__file__))[0] + ".ui"
        uic.loadUi(os.path.join(os.path.dirname(__file__), ui_file), self)

        # State
        self._features = []          # List of Feature objects in project
        self._feature_items = {}     # Mapping: QTreeWidgetItem → Feature
        self._menu_hierarchy = []    # Loaded menu hierarchy
        self._current_feature = None # Currently selected feature for editing
        self._undo_stack = []        # Undo stack of feature lists
        self._undo_pos = -1          # Current undo position
        self._param_widgets = {}     # Current parameter editor widgets

        # Preferences — sync with machine units
        self.pref = Preferences()
        self.pref.read("mill")
        self._sync_units()
        # Subscribe to unit changes so display stays in sync
        try:
            STATUS.linear_units.signal.connect(self._on_units_changed)
        except Exception:
            pass

        # Menu loader
        self.menu_loader = MenuLoader()

        # G-code generator
        self.generator = GCodeGenerator(self.pref)

        # Initialize UI
        self._setup_ui()
        self._set_catalog_from_machine()
        self._push_undo()

    def _setup_ui(self):
        """Wire up UI signals."""
        self.catalogCombo.currentTextChanged.connect(self._on_catalog_changed)
        self.buildButton.clicked.connect(self._on_build)
        self.exportButton.clicked.connect(self._on_export)
        self.addFeatureButton.clicked.connect(self._on_add_feature)
        self.deleteButton.clicked.connect(self._on_delete)
        self.duplicateButton.clicked.connect(self._on_duplicate)
        self.moveUpButton.clicked.connect(self._on_move_up)
        self.moveDownButton.clicked.connect(self._on_move_down)
        self.undoButton.clicked.connect(self._on_undo)
        self.redoButton.clicked.connect(self._on_redo)
        self.catalogTree.itemDoubleClicked.connect(self._on_add_feature)

        self.projectTree.currentItemChanged.connect(self._on_project_selection)
        self.projectTree.model().rowsMoved.connect(self._on_rows_moved)

        # Set up catalog tree header
        self.catalogTree.setColumnCount(1)
        self.projectTree.setColumnCount(1)

        # Timer for auto-refresh
        self._auto_refresh_timer = QTimer(self)
        self._auto_refresh_timer.timeout.connect(self._on_auto_refresh)
        self.autoRefreshCheck.toggled.connect(self._on_auto_refresh_toggled)

    # --- Units ---

    def _sync_units(self):
        """Sync preferences with current LinuxCNC machine linear units."""
        try:
            # STAT.linear_units: 1.0 = mm, 1/25.4 (~0.03937) = inch, 0.0 = N/A
            metric = STATUS.stat.linear_units == 2
            self.pref.set_machine_metric(metric)
            self.pref.set_default_metric(metric)
            LOG.debug("_sync_units: metric=%s (linear_units=%s)",
                      metric, STATUS.stat.linear_units)
        except Exception as e:
            LOG.debug("_sync_units: failed: %s", e)

    def _on_units_changed(self, value):
        """Callback when machine linear units change mid-session."""
        # value is the raw DataChannel signal payload (float)
        metric = float(value) >= 0.5  # 1.0 for mm, ~0.039 for inch
        LOG.debug("_on_units_changed: signal=%s metric=%s", value, metric)
        self.pref.set_machine_metric(metric)
        self.pref.set_default_metric(metric)

    # --- Catalog loading ---

    def _detect_machine_catalog(self):
        """Detect mill/lathe/plasma from LinuxCNC INI."""
        try:
            if INFO.getIsLathe():
                return "lathe"
            if INFO.ini.find('PLASMAC', 'MACHINE') or INFO.ini.find('PLASMAC', 'PRESSURE'):
                return "plasma"
        except Exception as e:
            LOG.debug("_detect_machine_catalog: failed: %s", e)
        return "mill"

    def _set_catalog_from_machine(self):
        """Set catalog combo to match detected machine type."""
        catalog = self._detect_machine_catalog()
        label_map = {"mill": "Mill", "lathe": "Lathe", "plasma": "Plasma"}
        label = label_map.get(catalog, "Mill")
        LOG.debug("_set_catalog_from_machine: detected %s -> %s", catalog, label)
        self.catalogCombo.setCurrentText(label)

    def _load_catalog(self, catalog_name):
        """Load and display a catalog menu."""
        self.catalogTree.clear()

        try:
            self._menu_hierarchy = []
            self.menu_loader.load(catalog_name, ncam_dir=feat.NCAM_DIR)
            self._menu_hierarchy = self.menu_loader.get_menu_hierarchy()
            self._build_catalog_tree(self.catalogTree, self._menu_hierarchy)
            self.catalogTree.expandAll()
        except Exception as e:
            LOG.error("Failed to load catalog '%s': %s", catalog_name, e)
            QMessageBox.warning(self, "Catalog Error",
                                "Could not load catalog: %s" % e)

    def _build_catalog_tree(self, parent, items):
        """Recursively build the catalog QTreeWidget from menu hierarchy."""
        for entry in items:
            if entry['is_menu']:
                # Submenu
                item = QTreeWidgetItem(parent)
                item.setText(0, entry['name'])
                if entry['icon']:
                    self._set_item_icon(item, entry['icon'])
                item.setFlags(item.flags() & ~Qt.ItemIsDragEnabled)
                self._build_catalog_tree(item, entry['children'])
            elif entry['src']:
                # Feature (has a .cfg file)
                item = QTreeWidgetItem(parent)
                item.setText(0, entry['name'])
                item.setToolTip(0, entry.get('tool_tip', ''))
                if entry['icon']:
                    self._set_item_icon(item, entry['icon'])
                # Store action and src for adding to project
                item.setData(0, Qt.UserRole, {
                    'action': entry['action'],
                    'src': entry['src'],
                })

    def _set_item_icon(self, item, icon_name):
        """Load and set an icon for a tree item."""
        if feat.NCAM_DIR:
            icon_path = os.path.join(feat.NCAM_DIR, 'graphics', icon_name)
            if os.path.isfile(icon_path):
                item.setIcon(0, QIcon(icon_path))

    def _on_catalog_changed(self, text):
        """Handle catalog combo box change."""
        catalog_map = {"Mill": "mill", "Lathe": "lathe", "Plasma": "plasma"}
        cat_name = catalog_map.get(text, "mill")
        self._load_catalog(cat_name)
        self.pref.read(cat_name)
        self._sync_units()  # re-apply machine units after catalog re-read

    # --- Project management ---

    def _on_add_feature(self, *args):
        """Add the selected catalog feature to the project."""
        item = self.catalogTree.currentItem()
        if item is None:
            return

        data = item.data(0, Qt.UserRole)
        if data is None or not data.get('src'):
            return

        src = data['src']
        cfg_path = search_path(True, src)
        if cfg_path is None:
            LOG.error("Config file not found: %s", src)
            QMessageBox.warning(self, "Error",
                                "Config file not found: %s" % src)
            return

        try:
            # Load feature from cfg
            feature = Feature(src=cfg_path)

            # Assign unique ID
            xml = self._features_to_xml()
            feature.get_id(xml)

            # Add to project
            self._features.append(feature)
            LOG.debug("_on_add_feature: added %s (id=%s, type=%s)",
                      feature.get_name(), id(feature), feature.get_type())
            self._rebuild_project_tree()
            self._push_undo()

            # Select the new feature
            last_item = self.projectTree.topLevelItem(
                self.projectTree.topLevelItemCount() - 1
            )
            if last_item:
                self.projectTree.setCurrentItem(last_item)

        except Exception as e:
            LOG.error("Failed to add feature: %s", e)
            QMessageBox.warning(self, "Error",
                                "Could not add feature: %s" % e)

    def _on_delete(self):
        """Delete selected feature from project."""
        item = self.projectTree.currentItem()
        if item is None:
            return

        feature = self._feature_items.get(id(item))
        if feature is None:
            return

        self._features.remove(feature)
        self._rebuild_project_tree()
        self._push_undo()
        self._clear_parameter_editor()

    def _on_duplicate(self):
        """Duplicate selected feature."""
        item = self.projectTree.currentItem()
        if item is None:
            return

        feature = self._feature_items.get(id(item))
        if feature is None:
            return

        # Deep copy the feature
        xml_copy = copy.deepcopy(feature.to_xml())
        new_feature = Feature(xml=xml_copy)

        # Assign new ID
        xml = self._features_to_xml()
        new_feature.get_id(xml)

        # Insert after current
        idx = self._features.index(feature)
        self._features.insert(idx + 1, new_feature)
        self._rebuild_project_tree()
        self._push_undo()

    def _on_move_up(self):
        """Move selected feature up."""
        item = self.projectTree.currentItem()
        if item is None:
            return
        feature = self._feature_items.get(id(item))
        if feature is None:
            return
        idx = self._features.index(feature)
        if idx > 0:
            self._features.pop(idx)
            self._features.insert(idx - 1, feature)
            self._rebuild_project_tree()
            self._push_undo()
            self._select_feature(feature)

    def _on_move_down(self):
        """Move selected feature down."""
        item = self.projectTree.currentItem()
        if item is None:
            return
        feature = self._feature_items.get(id(item))
        if feature is None:
            return
        idx = self._features.index(feature)
        if idx < len(self._features) - 1:
            self._features.pop(idx)
            self._features.insert(idx + 1, feature)
            self._rebuild_project_tree()
            self._push_undo()
            self._select_feature(feature)

    def _on_rows_moved(self):
        """Handle drag-drop reordering in project tree."""
        # Rebuild features list from tree order
        new_features = []
        for i in range(self.projectTree.topLevelItemCount()):
            item = self.projectTree.topLevelItem(i)
            feature = self._feature_items.get(id(item))
            if feature:
                new_features.append(feature)
        if new_features:
            self._features = new_features
            self._push_undo()

    # --- Project tree ---

    def _rebuild_project_tree(self):
        """Rebuild the project tree from self._features."""
        self.projectTree.blockSignals(True)
        self.projectTree.clear()
        self._feature_items.clear()

        for feature in self._features:
            item = QTreeWidgetItem(self.projectTree)
            item.setText(0, feature.get_name())
            item.setToolTip(0, feature.get_tooltip())
            item.setFlags(
                Qt.ItemIsSelectable | Qt.ItemIsEnabled |
                Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled
            )
            icon = feature.get_icon()
            if icon and feat.NCAM_DIR:
                icon_path = os.path.join(feat.NCAM_DIR, 'graphics', icon)
                if os.path.isfile(icon_path):
                    item.setIcon(0, QIcon(icon_path))
            self._feature_items[id(item)] = feature

        self.projectTree.blockSignals(False)

    def _on_project_selection(self, current, previous):
        """Handle project tree selection change."""
        if current is None:
            self._clear_parameter_editor()
            return

        feature = self._feature_items.get(id(current))
        if feature:
            LOG.debug("_on_project_selection: selected %s (id=%s, params=%d)",
                      feature.get_name(), id(feature), len(feature.param))
            self._current_feature = feature
            self._build_parameter_editor(feature)
        else:
            LOG.debug("_on_project_selection: feature not found for item id=%s", id(current))

    def _select_feature(self, feature):
        """Select a specific feature in the project tree."""
        for i in range(self.projectTree.topLevelItemCount()):
            item = self.projectTree.topLevelItem(i)
            if self._feature_items.get(id(item)) is feature:
                self.projectTree.setCurrentItem(item)
                break

    # --- Parameter editor ---

    def _build_parameter_editor(self, feature):
        """Build dynamic parameter editor widgets."""
        self._clear_parameter_editor()
        self._current_feature = feature
        self._param_widgets = {}
        layout = self.paramLayout

        for p in feature.param:
            p_type = p.get_type()
            header = p.get_header() or ''

            # Handle headers
            if p_type in ('header', 'sub-header'):
                if p_type == 'header':
                    lbl = QLabel("<b>%s</b>" % p.get_name())
                else:
                    lbl = QLabel("<i>%s</i>" % p.get_name())
                layout.addWidget(lbl)
                continue

            # Skip hidden params
            if p.get_hidden():
                continue

            # Create widget based on type
            row = QHBoxLayout()
            name_lbl = QLabel(p.get_name())
            name_lbl.setToolTip(p.get_tooltip())
            name_lbl.setMinimumWidth(120)
            row.addWidget(name_lbl)

            widget = self._create_param_widget(p)
            if widget:
                row.addWidget(widget, 1)
                layout.addLayout(row)
                self._param_widgets[p.get_call()] = widget

        layout.addStretch()

    def _create_param_widget(self, param):
        """Create the appropriate Qt widget for a parameter."""
        p_type = param.get_type()
        value = param.get_display_string()

        if p_type == 'bool':
            w = QCheckBox()
            w.setChecked(value in ('1', 'True', 'true'))
            w.toggled.connect(
                lambda checked, p=param: self._on_param_changed(p, '1' if checked else '0')
            )
            return w

        elif p_type == 'float':
            w = QDoubleSpinBox()
            w.setDecimals(param.get_digits())
            try:
                w.setMinimum(float(param.get_min_value()))
            except (ValueError, TypeError):
                w.setMinimum(-999999.9)
            try:
                w.setMaximum(float(param.get_max_value()))
            except (ValueError, TypeError):
                w.setMaximum(999999.9)
            try:
                w.setValue(float(value))
            except (ValueError, TypeError):
                w.setValue(0.0)
            w.valueChanged.connect(
                lambda v, p=param: self._on_param_changed(p, str(v))
            )
            return w

        elif p_type == 'int':
            w = QSpinBox()
            try:
                w.setMinimum(int(float(param.get_min_value())))
            except (ValueError, TypeError):
                w.setMinimum(-999999)
            try:
                w.setMaximum(int(float(param.get_max_value())))
            except (ValueError, TypeError):
                w.setMaximum(999999)
            try:
                w.setValue(int(float(value)))
            except (ValueError, TypeError):
                w.setValue(0)
            w.valueChanged.connect(
                lambda v, p=param: self._on_param_changed(p, str(v))
            )
            return w

        elif p_type in ('combo', 'combo-user'):
            w = QComboBox()
            options = param.get_options()
            if options:
                current_val = param.attr.get('value', '')
                selected_idx = 0
                for i, opt in enumerate(options.split(':')):
                    parts = opt.split('=', 1)
                    display = parts[0] if len(parts) > 0 else opt
                    opt_val = parts[1] if len(parts) > 1 else opt
                    w.addItem(display, opt_val)
                    if opt_val == current_val:
                        selected_idx = i
                w.setCurrentIndex(selected_idx)
            w.currentIndexChanged.connect(
                lambda idx, p=param, cb=w: self._on_param_changed(
                    p, cb.itemData(idx) or str(idx)
                )
            )
            return w

        elif p_type == 'gcode':
            w = QPlainTextEdit()
            w.setMaximumHeight(80)
            w.setPlainText(value)
            def _on_gcode_done():
                self._on_param_changed(param, w.toPlainText())
            w.installEventFilter(_FocusLostFilter(_on_gcode_done))
            return w

        elif p_type == 'text':
            w = QPlainTextEdit()
            w.setMaximumHeight(80)
            w.setPlainText(value)
            def _on_text_done():
                self._on_param_changed(param, w.toPlainText())
            w.installEventFilter(_FocusLostFilter(_on_text_done))
            return w

        elif p_type == 'list':
            w = QComboBox()
            options = param.get_options()
            if options:
                current_val = param.attr.get('value', '')
                selected_idx = 0
                for i, opt in enumerate(options.split(':')):
                    parts = opt.split('=', 1)
                    display = parts[0] if len(parts) > 0 else opt
                    opt_val = parts[1] if len(parts) > 1 else opt
                    w.addItem(display, opt_val)
                    if opt_val == current_val:
                        selected_idx = i
                w.setCurrentIndex(selected_idx)
            w.currentIndexChanged.connect(
                lambda idx, p=param, cb=w: self._on_param_changed(
                    p, cb.itemData(idx) or str(idx)
                )
            )
            return w

        else:
            # Default: string line edit
            w = QLineEdit()
            w.setText(str(value))
            w.textChanged.connect(
                lambda v, p=param: self._on_param_changed(p, v)
            )
            return w

    def _on_param_changed(self, param, new_value):
        """Handle a parameter value change."""
        feature = self._current_feature
        if feature is None:
            LOG.warning("_on_param_changed: _current_feature is None!")
            return
        old_raw = param.attr.get('value', '?')
        ok = param.set_value(new_value, feature)
        LOG.debug("_on_param_changed: %s %s old=%s new=%s ok=%s feat=%s",
                  param.get_call(), param.get_name(), old_raw, new_value, ok,
                  feature.get_name())
        if ok:
            self._push_undo()
            if param.get_name() == 'Name' or param.get_call() == '#param_name':
                self._rebuild_project_tree()

    def _clear_parameter_editor(self):
        """Clear the parameter editor panel."""
        self._param_widgets = {}
        self._current_feature = None

        layout = self.paramLayout
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)
            elif item.layout():
                self._clear_layout(item.layout())

    def _clear_layout(self, layout):
        """Recursively clear a layout."""
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)
            elif item.layout():
                self._clear_layout(item.layout())

    # --- G-code generation ---

    def _on_build(self):
        """Generate G-code and show preview."""
        try:
            # Log current feature values for debugging
            for f in self._features:
                for p in f.param:
                    if p.get_type() in ('float', 'int', 'combo', 'bool'):
                        LOG.debug("build: %s %s = %s", f.get_name(),
                                  p.get_call(), p.attr.get('value', '?'))
            xml = self._features_to_xml()
            gcode = self.generator.generate(xml)
            self.gcodePreview.setPlainText(gcode)

            # If auto-refresh is on, load into LinuxCNC
            if self.autoRefreshCheck.isChecked():
                self._load_into_linuxcnc(gcode)
        except Exception as e:
            LOG.error("Build failed: %s", e)
            QMessageBox.critical(self, "Build Error",
                                 "Failed to generate G-code:\n%s" % e)

    def _on_export(self):
        """Export G-code to file."""
        xml = self._features_to_xml()
        gcode = self.generator.generate(xml)

        filename, _ = QFileDialog.getSaveFileName(
            self, "Export G-code",
            os.path.expanduser("~"),
            "NGC files (*.ngc);;All files (*)"
        )
        if filename:
            if not filename.endswith('.ngc'):
                filename += '.ngc'
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(gcode)
                self.gcodePreview.setPlainText(gcode)
                LOG.info("Exported to: %s", filename)
            except Exception as e:
                QMessageBox.critical(self, "Export Error",
                                     "Could not write file:\n%s" % e)

    def _load_into_linuxcnc(self, gcode):
        """Load generated G-code into LinuxCNC."""
        output_path = None
        if feat.NCAM_DIR:
            import nativecam_core.gcode_generator as gg
            gg.NCAM_DIR = feat.NCAM_DIR
            nc_dir = os.path.join(feat.NCAM_DIR, gg.NGC_DIR)
        else:
            nc_dir = os.path.join(
                os.path.expanduser("~"), "nativecam", "scripts"
            )

        os.makedirs(nc_dir, exist_ok=True)
        output_path = os.path.join(nc_dir, GENERATED_FILE)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(gcode)

        # Try to load into LinuxCNC
        try:
            import linuxcnc
            c = linuxcnc.command()
            s = linuxcnc.stat()
            s.poll()
            if s.interp_state == linuxcnc.INTERP_IDLE:
                c.reset_interpreter()
                c.mode(linuxcnc.MODE_AUTO)
                import time
                time.sleep(0.3)
                s.poll()
                if s.task_mode == linuxcnc.MODE_AUTO:
                    c.program_open(output_path)
                    LOG.info("Loaded G-code into LinuxCNC: %s", output_path)
                else:
                    LOG.warning("Could not switch LinuxCNC to AUTO mode")
            else:
                LOG.warning("LinuxCNC interpreter not idle")
        except Exception as e:
            LOG.debug("Cannot load into LinuxCNC (not running?): %s", e)

    def _on_auto_refresh_toggled(self, checked):
        """Start/stop auto-refresh timer."""
        if checked:
            self._auto_refresh_timer.start(2000)  # Every 2 seconds
        else:
            self._auto_refresh_timer.stop()

    def _on_auto_refresh(self):
        """Auto-refresh: rebuild G-code and load."""
        self._on_build()

    # --- Undo/redo ---

    def _push_undo(self):
        """Push current state to undo stack."""
        self._undo_stack = self._undo_stack[:self._undo_pos + 1]
        state = [Feature(xml=copy.deepcopy(f.to_xml())) for f in self._features]
        self._undo_stack.append(state)
        self._undo_pos = len(self._undo_stack) - 1

        if len(self._undo_stack) > 200:
            self._undo_stack.pop(0)
            self._undo_pos -= 1

    def _on_undo(self):
        """Undo last action."""
        if self._undo_pos <= 0:
            return
        self._undo_pos -= 1
        self._features = [
            Feature(xml=copy.deepcopy(f.to_xml()))
            for f in self._undo_stack[self._undo_pos]
        ]
        self._rebuild_project_tree()
        self._clear_parameter_editor()

    def _on_redo(self):
        """Redo last undone action."""
        if self._undo_pos >= len(self._undo_stack) - 1:
            return
        self._undo_pos += 1
        self._features = [
            Feature(xml=copy.deepcopy(f.to_xml()))
            for f in self._undo_stack[self._undo_pos]
        ]
        self._rebuild_project_tree()
        self._clear_parameter_editor()

    # --- Helpers ---

    def _features_to_xml(self):
        """Convert current features list to XML tree."""
        xml = ET.Element("lcnc-ncam")
        for f in self._features:
            xml.append(f.to_xml())
        return xml
