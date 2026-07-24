# "Polygon"

>"<b>Create a Polygon with n edges</b>"

| | |
|---|---|
| Type | `polygon` |
| Icon | `hexagon.png` |
| Source | `mill/polygon.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(polygon of #param_n edges author : Fernand Veilleux)

o<#self_id_active> if [#param_act] (if active)
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<polygon> CALL [#param_cx] [#param_cy] [#param_n] [#param_r] [#param_rot] [#param_opt] [#param_dir] [#31] [#32] [#param_pv] [#param_fp] [#param_fcs] [#param_xa]

o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords"** | | |
| 4 | "cX" | Float | `0.0000` |
| 5 | "cY" | Float | `0.0000` |
| | **"Size, rotation"** | | |
| 7 | "Edges count" | Integer | `6` |
| 8 | "Radius" | Float | `1.0000` |
| 9 | "Rotation" | Float | `0.00` |
| | **"Milling"** | | |
| 11 | "Option" | Dropdown | `0` |
| 12 | "Arc lead-out" | Toggle | `1` |
| 13 | "Direction" | Dropdown | `3` |
| 14 | "Cut start" | Dropdown (editable) | `1` |
| 15 | "User start" | Float | `0.0000` |
| 16 | User gcode | G-code | `` |
| 17 | "Cut down to" | Dropdown (editable) | `1` |
| 18 | "User depth" | Float | `-0.5000` |
| 19 | User depth gcode | G-code | `` |
| | **"Finishing"** | | |
| 21 | "Finishing pass" | Dropdown | `0` |
| 22 | "Finishing cut" | Float | `0.0400` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_pv`
- "Show design"

### "cX"
- **NGC variable**: `#param_cx`
- "Polygon center X"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "cY"
- **NGC variable**: `#param_cy`
- "Polygon center Y"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Edges count"
- **NGC variable**: `#param_n`
- "Number of edges"

### "Radius"
- **NGC variable**: `#param_r`
- "Radius"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Rotation"
- **NGC variable**: `#param_rot`
- "Start angle"
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
- **NGC variable**: `#param_fcs`
- "Last finishing cut"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(polygon of #param_n edges author : Fernand Veilleux)

o<#self_id_active> if [#param_act] (if active)
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<polygon> CALL [#param_cx] [#param_cy] [#param_n] [#param_r] [#param_rot] [#param_opt] [#param_dir] [#31] [#32] [#param_pv] [#param_fp] [#param_fcs] [#param_xa]

o<#self_id_active> endif
(end #sub_name)
```
