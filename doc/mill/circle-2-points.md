# "Circle 2 points"

>"<b>Create a Circle by defining ends of diameter</b>&#10;Points are the ends of the diameter and can add a flat"

| | |
|---|---|
| Type | `circle-2` |
| Icon | `circle-2.png` |
| Source | `mill/circle-2.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(circle from ends of diameter author : Fernand Veilleux)

o<#self_id_active> if [#param_act] (if active)
	#<flat#ID> = [#param_f]
	#<delx#ID> = [#param_x2 - #param_x1]
	#<dely#ID> = [#param_y2 - #param_y1]
	#<diameter#ID> = [SQRT[#<delx#ID> * #<delx#ID> + #<dely#ID> * #<dely#ID>]]
	#<cx#ID> = [[#param_x1 + #param_x2] / 2]
	#<cy#ID> = [[#param_y1 + #param_y2] / 2]

	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<circle> CALL [#<cx#ID>] [#<cy#ID>] [#<diameter#ID>] [#<flat#ID>] [#param_rot] [#param_opt] [#param_dir] [#31] [#32] [#param_fcut] [#param_fp] [#param_fc] [#param_xa]

o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords"** | | |
| 4 | "X1" | Float | `0.0000` |
| 5 | "Y1" | Float | `0.0000` |
| 6 | "X2" | Float | `2.0000` |
| 7 | "Y2" | Float | `1.0000` |
| | **"D flat"** | | |
| 9 | "Remove" | Float | `0.0000` |
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
- **NGC variable**: `#param_fcut`
- "Show design"

### "X1"
- **NGC variable**: `#param_x1`
- "One end of the diameter"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y1"
- **NGC variable**: `#param_y1`
- "One end of the diameter"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X2"
- **NGC variable**: `#param_x2`
- "Opposite end of the diameter"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y2"
- **NGC variable**: `#param_y2`
- "Opposite end of the diameter"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

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
- **NGC variable**: `#param_fc`
- "Last finishing cut"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(circle from ends of diameter author : Fernand Veilleux)

o<#self_id_active> if [#param_act] (if active)
	#<flat#ID> = [#param_f]
	#<delx#ID> = [#param_x2 - #param_x1]
	#<dely#ID> = [#param_y2 - #param_y1]
	#<diameter#ID> = [SQRT[#<delx#ID> * #<delx#ID> + #<dely#ID> * #<dely#ID>]]
	#<cx#ID> = [[#param_x1 + #param_x2] / 2]
	#<cy#ID> = [[#param_y1 + #param_y2] / 2]

	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<circle> CALL [#<cx#ID>] [#<cy#ID>] [#<diameter#ID>] [#<flat#ID>] [#param_rot] [#param_opt] [#param_dir] [#31] [#32] [#param_fcut] [#param_fp] [#param_fc] [#param_xa]

o<#self_id_active> endif
(end #sub_name)
```
