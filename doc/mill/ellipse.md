# "Ellipse"

>"<b>Create an Ellipse</b>"

| | |
|---|---|
| Type | `ellipse` |
| Icon | `ellipse.png` |
| Source | `mill/ellipse.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(ellipse author : Fernand Veilleux)

o<#self_id_active> if [#param_act]
	o<#self_id_00> if [#param_xr LT #param_yr] (if narrower than high)
		#<xr#ID>   = [#param_yr]
		#<yr#ID>   = [#param_xr]
		o<select> CALL [32] [#param_al_y] [-#<xr#ID>] [0] [#<xr#ID>]
		o<select> CALL [31] [#param_al_x] [-#<yr#ID>] [0] [#<yr#ID>]
		#<rot#ID> = [90.0 + #param_rot]

	o<#self_id_00> else
		#<xr#ID>   = [#param_xr]
		#<yr#ID>   = [#param_yr]
		o<select> CALL [32] [#param_al_x] [#<xr#ID>]  [0] [-#<xr#ID>]
		o<select> CALL [31] [#param_al_y] [-#<yr#ID>] [0] [#<yr#ID>]
		#<rot#ID> = #param_rot
	o<#self_id_00> endif

	o<select> CALL [33] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [34] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<ellipse> CALL [#param_cx] [#param_cy] [#<xr#ID>] [#<yr#ID>] [#<rot#ID>] [#32] [#31] [#param_seg] [#param_opt] [#param_dir] [#33] [#34] [#param_pv] [#param_fp] [#param_fcs] [#param_xa]

o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords"** | | |
| 4 | "X" | Float | `0.0000` |
| 5 | "X axis align" | Dropdown | `1` |
| 6 | "Y" | Float | `0.0000` |
| 7 | "Y axis align" | Dropdown | `1` |
| | **"Size, rotation"** | | |
| 9 | "Control points" | Integer | `30` |
| 10 | "X Radius" | Float | `2.0000` |
| 11 | "Y Radius" | Float | `1.0000` |
| 12 | "Rotation" | Float | `0.00` |
| | **"Milling"** | | |
| 14 | "Option" | Dropdown | `0` |
| 15 | "Arc lead-out" | Toggle | `1` |
| 16 | "Direction" | Dropdown | `3` |
| 17 | "Cut start" | Dropdown (editable) | `1` |
| 18 | "User start" | Float | `0.0000` |
| 19 | User gcode | G-code | `` |
| 20 | "Cut down to" | Dropdown (editable) | `1` |
| 21 | "User depth" | Float | `-0.5000` |
| 22 | User depth gcode | G-code | `` |
| | **"Finishing"** | | |
| 24 | "Finishing pass" | Dropdown | `0` |
| 25 | "Finishing cut" | Float | `0.0400` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_pv`
- "Show design"

### "X"
- **NGC variable**: `#param_cx`
- "Center of ellipse"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X axis align"
- **NGC variable**: `#param_al_x`
- "Define X reference point"
- **Options**: "Left=0:Center=1:Right=2"

### "Y"
- **NGC variable**: `#param_cy`
- "Center of ellipse"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y axis align"
- **NGC variable**: `#param_al_y`
- "Define Y reference point"
- **Options**: "Top=0:Center=1:Bottom=2"

### "Control points"
- **NGC variable**: `#param_seg`
- "Per quadrant, smoother with more"

### "X Radius"
- **NGC variable**: `#param_xr`
- "Radius in X axis"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Y Radius"
- **NGC variable**: `#param_yr`
- "Radius in Y axis"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

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
(ellipse author : Fernand Veilleux)

o<#self_id_active> if [#param_act]
	o<#self_id_00> if [#param_xr LT #param_yr] (if narrower than high)
		#<xr#ID>   = [#param_yr]
		#<yr#ID>   = [#param_xr]
		o<select> CALL [32] [#param_al_y] [-#<xr#ID>] [0] [#<xr#ID>]
		o<select> CALL [31] [#param_al_x] [-#<yr#ID>] [0] [#<yr#ID>]
		#<rot#ID> = [90.0 + #param_rot]

	o<#self_id_00> else
		#<xr#ID>   = [#param_xr]
		#<yr#ID>   = [#param_yr]
		o<select> CALL [32] [#param_al_x] [#<xr#ID>]  [0] [-#<xr#ID>]
		o<select> CALL [31] [#param_al_y] [-#<yr#ID>] [0] [#<yr#ID>]
		#<rot#ID> = #param_rot
	o<#self_id_00> endif

	o<select> CALL [33] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [34] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<ellipse> CALL [#param_cx] [#param_cy] [#<xr#ID>] [#<yr#ID>] [#<rot#ID>] [#32] [#31] [#param_seg] [#param_opt] [#param_dir] [#33] [#34] [#param_pv] [#param_fp] [#param_fcs] [#param_xa]

o<#self_id_active> endif
(end #sub_name)
```
