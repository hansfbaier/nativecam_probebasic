# "Probe Workpiece"

>"<b>Probe X and Y axis differently inside or outside with options for touch-off&#10;START WITH PROBE IN CENTER OF WORK PIECE</b>&#10;<span foreground='blue' style='oblique'><b>Message possible in terminal window</b></span>"

| | |
|---|---|
| Type | `probe_stock` |
| Icon | `probe-stock.png` |
| Source | `mill/probe-stock.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(probe material author : Fernand Veilleux)

o<#self_id_ena> if [#param_act]
	o<probe_stock> CALL [#param_xopt] [#param_yopt] [#param_el] [#param_clr] [#param_xz] [#param_yz] [#param_dbx] [#param_dby] [#param_al_x] [#param_al_y] [#param_touch] [#param_info] [#<wp_inside_length>] [#<wp_length>] [#<wp_inside_width>] [#<wp_width>] [#param_zopt] [#param_zval] [#param_zdepth]

o<#self_id_ena> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show entry lines" | Toggle | `1` |
| | **"X axis"** | | |
| 4 | "Mode" | Dropdown | `1` |
| 5 | "Probe height" | Float | `-0.5000` |
| 6 | "Double check" | Toggle | `0` |
| | **"Y axis"** | | |
| 8 | "Mode" | Dropdown | `0` |
| 9 | "Probe height" | Float | `0.0000` |
| 10 | "Double check" | Toggle | `0` |
| | **"Z axis"** | | |
| 12 | "Probe axis" | Dropdown | `0` |
| 13 | "Set value" | Float | `0.0000` |
| 14 | "Depth" | Float | `-0.4000` |
| | **"Touching off"** | | |
| 16 | "Touch off X,Y" | Toggle | `1` |
| 17 | "X axis align" | Dropdown | `1` |
| 18 | "Y axis align" | Dropdown | `1` |
| | **"Options"** | | |
| 20 | "Safe relative Z" | Float | `0.5000` |
| 21 | "Calibration info" | Toggle | `0` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show entry lines"
- **NGC variable**: `#param_el`
- "Show entry lines"

### "Mode"
- **NGC variable**: `#param_xopt`
- "Probe inside or outside"
- **Options**: "Inside=0:Outside=1"

### "Probe height"
- **NGC variable**: `#param_xz`
- "Relative to start position"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Double check"
- **NGC variable**: `#param_dbx`
- "Double check"

### "Mode"
- **NGC variable**: `#param_yopt`
- "Probe inside or outside"
- **Options**: "Inside=0:Outside=1"

### "Probe height"
- **NGC variable**: `#param_yz`
- "Relative to start position"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Double check"
- **NGC variable**: `#param_dby`
- "Only if X is double checked"

### "Probe axis"
- **NGC variable**: `#param_zopt`
- "Do NOT Probe if hollow"
- **Options**: "No=0:Yes and set height=1:Yes and do not set=2"

### "Set value"
- **NGC variable**: `#param_zval`
- "Value to set if touch"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Depth"
- **NGC variable**: `#param_zdepth`
- "Maximum depth"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Touch off X,Y"
- **NGC variable**: `#param_touch`
- "Set center to X0 and Y0"

### "X axis align"
- **NGC variable**: `#param_al_x`
- "Define X reference point"
- **Options**: "Left=0:Center=1:Right=2"

### "Y axis align"
- **NGC variable**: `#param_al_y`
- "Define Y reference point"
- **Options**: "Top=0:Center=1:Bottom=2"

### "Safe relative Z"
- **NGC variable**: `#param_clr`
- "Relative to start position"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Calibration info"
- **NGC variable**: `#param_info`
- "Show calibration helpful info"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(probe material author : Fernand Veilleux)

o<#self_id_ena> if [#param_act]
	o<probe_stock> CALL [#param_xopt] [#param_yopt] [#param_el] [#param_clr] [#param_xz] [#param_yz] [#param_dbx] [#param_dby] [#param_al_x] [#param_al_y] [#param_touch] [#param_info] [#<wp_inside_length>] [#<wp_length>] [#<wp_inside_width>] [#<wp_width>] [#param_zopt] [#param_zval] [#param_zdepth]

o<#self_id_ena> endif
(end #sub_name)
```
