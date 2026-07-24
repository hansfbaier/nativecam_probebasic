# "Slot/oval 1 point"

>"<b>Creates a Slot from a single point</b>&#10;Reference point can be center of slot or of one end"

| | |
|---|---|
| Type | `slot` |
| Icon | `slot.png` |
| Source | `mill/slot.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(slot from center or end author: Fernand Veilleux)

o<#self_id_active> if [#param_act] (if active)
	#<l#ID>   = [#param_l]
	#<w#ID>   = [#param_w]
	#<fcs#ID> = [#param_fcs]

	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<select> CALL [33] [#param_ref] [#<l#ID> / 2] [0]

	o<rectangle> CALL [#param_x] [#param_y] [#<l#ID> + #<w#ID>] [#<w#ID>] [#param_rot] [#33] [0] [1] [#<w#ID> / 2] [#param_opt] [#param_dir] [#31] [#32] [#param_pv] [#param_fp] [#<fcs#ID>] [#param_xa]

o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords"** | | |
| 4 | "X" | Float | `0.0000` |
| 5 | "X axis align" | Dropdown | `0` |
| 6 | "Y" | Float | `0.0000` |
| | **"Size, rotation"** | | |
| 8 | "Width" | Float | `0.5000` |
| 9 | "Effective length" | Float | `1.0000` |
| 10 | "Rotation" | Float | `0.00` |
| | **"Milling"** | | |
| 12 | "Option" | Dropdown | `0` |
| 13 | "Arc lead-out" | Toggle | `1` |
| 14 | "Direction" | Dropdown | `3` |
| 15 | "Cut start" | Dropdown (editable) | `1` |
| 16 | "User start" | Float | `0.0000` |
| 17 | User gcode | G-code | `` |
| 18 | "Cut down to" | Dropdown (editable) | `1` |
| 19 | "User depth" | Float | `-0.5000` |
| 20 | User depth gcode | G-code | `` |
| | **"Finishing"** | | |
| 22 | "Finishing pass" | Dropdown | `0` |
| 23 | "Finishing cut" | Float | `0.0400` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_pv`
- "Show design"

### "X"
- **NGC variable**: `#param_x`
- "X Center"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X axis align"
- **NGC variable**: `#param_ref`
- "X,Y center of slot or left end"
- **Options**: "End=0:Center of slot=1"

### "Y"
- **NGC variable**: `#param_y`
- "Y center"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Width"
- **NGC variable**: `#param_w`
- "Width of slot"
- **Min**: 0  **Max**: 999999.9  **Digits**: 4

### "Effective length"
- **NGC variable**: `#param_l`
- "Length between center of arcs"
- **Min**: 0  **Max**: 999999.9  **Digits**: 4

### "Rotation"
- **NGC variable**: `#param_rot`
- "Angle rotated"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Option"
- **NGC variable**: `#param_opt`
- "Select tool path"
- **Options**: "Inside normal=0:Pocket=1:On the line=2:Outside=3"

### "Arc lead-out"
- **NGC variable**: `#param_xa`
- "Not if on the line"

### "Direction"
- **NGC variable**: `#param_dir`
- "Direction of tool path"
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
(slot from center or end author: Fernand Veilleux)

o<#self_id_active> if [#param_act] (if active)
	#<l#ID>   = [#param_l]
	#<w#ID>   = [#param_w]
	#<fcs#ID> = [#param_fcs]

	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<select> CALL [33] [#param_ref] [#<l#ID> / 2] [0]

	o<rectangle> CALL [#param_x] [#param_y] [#<l#ID> + #<w#ID>] [#<w#ID>] [#param_rot] [#33] [0] [1] [#<w#ID> / 2] [#param_opt] [#param_dir] [#31] [#32] [#param_pv] [#param_fp] [#<fcs#ID>] [#param_xa]

o<#self_id_active> endif
(end #sub_name)
```
