# "Circle by Center"

>"<b>Create a Circle from it's center</b>&#10;Can add a flat"

| | |
|---|---|
| Type | `circle` |
| Icon | `circle.png` |
| Source | `mill/circle.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(circle from center author : Fernand Veilleux)

o<#self_id_active> if [#param_act] (if active)
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<select> CALL [33] [#param_al_x] [#param_d / 2] [0] [-#param_d / 2]
	o<select> CALL [34] [#param_al_y] [-#param_d / 2] [0] [#param_d / 2]

	o<circle> CALL [#param_cx + #33] [#param_cy + #34] [#param_d] [#param_f] [#param_rot] [#param_opt] [#param_dir] [#31] [#32] [#param_pv] [#param_fp] [#param_fc] [#param_xa]

o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords, size"** | | |
| 4 | "cX" | Float | `0.0000` |
| 5 | "X axis align" | Dropdown | `1` |
| 6 | "cY" | Float | `0.0000` |
| 7 | "Y axis align" | Dropdown | `1` |
| 8 | "Diameter" | Float | `1.5000` |
| | **"D flat"** | | |
| 10 | "Remove" | Float | `0.0000` |
| 11 | "Rotation" | Float | `0.00` |
| | **"Milling"** | | |
| 13 | "Option" | Dropdown | `0` |
| 14 | "Arc lead-out" | Toggle | `1` |
| 15 | "Direction" | Dropdown | `3` |
| 16 | "Cut start" | Dropdown (editable) | `1` |
| 17 | User start | Float | `0.0000` |
| 18 | User gcode | G-code | `` |
| 19 | "Cut down to" | Dropdown (editable) | `1` |
| 20 | User depth | Float | `-0.5000` |
| 21 | User depth gcode | G-code | `` |
| | **"Finishing"** | | |
| 23 | "Finishing pass" | Dropdown | `0` |
| 24 | "Finishing cut" | Float | `0.0400` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_pv`
- "Show design"

### "cX"
- **NGC variable**: `#param_cx`
- "Center of circle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X axis align"
- **NGC variable**: `#param_al_x`
- "Define X reference point"
- **Options**: "Left=0:Center=1:Right=2"

### "cY"
- **NGC variable**: `#param_cy`
- "Center of circle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y axis align"
- **NGC variable**: `#param_al_y`
- "Define Y reference point"
- **Options**: "Top=0:Center=1:Bottom=2"

### "Diameter"
- **NGC variable**: `#param_d`
- "Diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Remove"
- **NGC variable**: `#param_f`
- "Height to remove from diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Rotation"
- **NGC variable**: `#param_rot`
- "Rotation of flat"
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
- "Direction of path"
- **Options**: "Clockwise=2:Counter-Clockwise=3"

### "Cut start"
- **NGC variable**: `#param_s`
- "Pre or user defined"
- **Options**: "User defined=0:Surface=1:Half=2:One quarter=3:Three quarter=4:G-Code=5"

### User start
- **NGC variable**: `#param_u_s`
- User start
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### User gcode
- **NGC variable**: `#param_ugc`
- User gcode

### "Cut down to"
- **NGC variable**: `#param_dpt`
- "Pre or user defined"
- **Options**: "User defined=0:Through=1:Bottom=2:Half=3:One quarter=4:Three quarter=5:G-Code=6"

### User depth
- **NGC variable**: `#param_u_dpt`
- User depth
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### User depth gcode
- **NGC variable**: `#param_ugcd`
- User depth gcode

### "Finishing pass"
- **NGC variable**: `#param_fp`
- "Conventional for better finish"
- **Options**: "None=0:Clockwise=2:Clockwise full depth=12:Counter-Clockwise=3:Counter-Clockwise full depth=13"

### "Finishing cut"
- **NGC variable**: `#param_fc`
- "Last finishing cut"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(circle from center author : Fernand Veilleux)

o<#self_id_active> if [#param_act] (if active)
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<select> CALL [33] [#param_al_x] [#param_d / 2] [0] [-#param_d / 2]
	o<select> CALL [34] [#param_al_y] [-#param_d / 2] [0] [#param_d / 2]

	o<circle> CALL [#param_cx + #33] [#param_cy + #34] [#param_d] [#param_f] [#param_rot] [#param_opt] [#param_dir] [#31] [#32] [#param_pv] [#param_fp] [#param_fc] [#param_xa]

o<#self_id_active> endif
(end #sub_name)
```
