# "Slot/oval 2 points"

>"<b>Creates a Slot between two end points</b>"

| | |
|---|---|
| Type | `slot-2points` |
| Icon | `slot-2.png` |
| Source | `mill/slot-2.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(slot between two points author : Fernand Veilleux)

o<#self_id_active> if [#param_act] (if active)
	#<w#ID>   = [#param_w]
	#<fcs#ID> = [#param_fcs]

	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<line> CALL [#param_x1] [#param_y1] [#param_x2] [#param_y2]
	o<rectangle> CALL [#param_x1] [#param_y1] [#<_line_len> + #<w#ID>] [#<w#ID>] [#<_line_phi>] [#<_line_len> / 2] [0] [1] [#<w#ID> / 2] [#param_opt] [#param_dir] [#31] [#32] [#param_fc] [#param_fp] [#<fcs#ID>] [#param_xa]

	o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords, size"** | | |
| 4 | "X1" | Float | `0.0000` |
| 5 | "Y1" | Float | `0.0000` |
| 6 | "X2" | Float | `2.0000` |
| 7 | "Y2" | Float | `1.0000` |
| 8 | "Width" | Float | `0.5000` |
| | **"Milling"** | | |
| 10 | "Option" | Dropdown | `0` |
| 11 | "Arc lead-out" | Toggle | `1` |
| 12 | "Direction" | Dropdown | `3` |
| 13 | "Cut start" | Dropdown (editable) | `1` |
| 14 | "User start" | Float | `0.0000` |
| 15 | User gcode | G-code | `` |
| 16 | "Cut down to" | Dropdown (editable) | `1` |
| 17 | "User depth" | Float | `-0.5000` |
| 18 | User depth gcode | G-code | `` |
| | **"Finishing"** | | |
| 20 | "Finishing pass" | Dropdown | `0` |
| 21 | "Finishing cut" | Float | `0.0400` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_fc`
- "Show design"

### "X1"
- **NGC variable**: `#param_x1`
- "First point"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y1"
- **NGC variable**: `#param_y1`
- "First point"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X2"
- **NGC variable**: `#param_x2`
- "Second point"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y2"
- **NGC variable**: `#param_y2`
- "Second point"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Width"
- **NGC variable**: `#param_w`
- "Width of slot"
- **Min**: 0  **Max**: 999999.9  **Digits**: 4

### "Option"
- **NGC variable**: `#param_opt`
- "Select tool path"
- **Options**: "Inside normal=0:Pocket=1:On the line=2:Outside=3"

### "Arc lead-out"
- **NGC variable**: `#param_xa`
- "Not if on the line"

### "Direction"
- **NGC variable**: `#param_dir`
- "Direction of path"
- **Options**: "Clockwise=2:Counter-Clockwise=3"

### "Cut start"
- **NGC variable**: `#param_s`
- "Pre or user defined"
- **Options**: "User defined=0:Surface=1:Half=2:One quarter=3:Three quarter=4:G-Code=5"

### "User start"
- **NGC variable**: `#param_u_s`
- "User start"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### User gcode
- **NGC variable**: `#param_ugc`
- User gcode

### "Cut down to"
- **NGC variable**: `#param_dpt`
- "Pre or user defined"
- **Options**: "User defined=0:Through=1:Bottom=2:Half=3:One quarter=4:Three quarter=5:G-Code=6"

### "User depth"
- **NGC variable**: `#param_u_dpt`
- "User depth"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### User depth gcode
- **NGC variable**: `#param_ugcd`
- User depth gcode

### "Finishing pass"
- **NGC variable**: `#param_fp`
- "Conventional for better finish"
- **Options**: "None=0:Clockwise=2:Clockwise full depth=12:Counter-Clockwise=3:Counter-Clockwise full depth=13"

### "Finishing cut"
- **NGC variable**: `#param_fcs`
- "Last finishing cut"
- **Min**: 0.01  **Max**: 999999.9  **Digits**: 4

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(slot between two points author : Fernand Veilleux)

o<#self_id_active> if [#param_act] (if active)
	#<w#ID>   = [#param_w]
	#<fcs#ID> = [#param_fcs]

	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<line> CALL [#param_x1] [#param_y1] [#param_x2] [#param_y2]
	o<rectangle> CALL [#param_x1] [#param_y1] [#<_line_len> + #<w#ID>] [#<w#ID>] [#<_line_phi>] [#<_line_len> / 2] [0] [1] [#<w#ID> / 2] [#param_opt] [#param_dir] [#31] [#32] [#param_fc] [#param_fp] [#<fcs#ID>] [#param_xa]

	o<#self_id_active> endif
(end #sub_name)
```
