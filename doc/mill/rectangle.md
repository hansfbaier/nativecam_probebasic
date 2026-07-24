# "Rectangle"

>"<b>Create a Rectangle and align X and Y</b>&#10;Corners can be radiused or beveled"

| | |
|---|---|
| Type | `rectangle` |
| Icon | `center-rect.png` |
| Source | `mill/rectangle.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(rectangle author : Fernand Veilleux)

o<#self_id_active> if [#param_act]
	o<#self_id_00> if [#param_h GT #param_w] (if narrower than high)
		#<h#ID>   = [#param_w]
		#<w#ID>   = [#param_h]
		#<rot#ID> = [90.0 + #param_rot]
		o<select> CALL [31] [#param_al_x] [-#<h#ID> / 2] [0] [#<h#ID> / 2]
		o<select> CALL [32] [#param_al_y] [-#<w#ID> / 2] [0] [#<w#ID> / 2]

	o<#self_id_00> else
		#<w#ID>   = [#param_w]
		#<h#ID>   = [#param_h]
		#<rot#ID> = #param_rot
		o<select> CALL [32] [#param_al_x] [#<w#ID> / 2] [0] [-#<w#ID> / 2]
		o<select> CALL [31] [#param_al_y] [-#<h#ID> / 2] [0] [#<h#ID> / 2]
	o<#self_id_00> endif

	#<fcs#ID> = [#param_fcs]
	o<get_min> CALL [37] [2] [#param_cr] [#<h#ID> / 2]

	o<select> CALL [33] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [34] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<rectangle> CALL [#param_x] [#param_y] [#<w#ID>] [#<h#ID>] [#<rot#ID>] [#32] [#31] [#param_ct] [#37] [#param_opt] [#param_dir] [#33] [#34] [#param_pv] [#param_fp] [#<fcs#ID>] [#param_xa]

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
| 7 | "Y axis align" | Dropdown | `2` |
| | **"Size, rotation"** | | |
| 9 | "Width" | Float | `3.0000` |
| 10 | "Height" | Float | `2.0000` |
| 11 | "Rotation" | Float | `0.00` |
| | **"Corners"** | | |
| 13 | "Type" | Dropdown | `0` |
| 14 | "Radius" | Float | `0.0000` |
| | **"Milling"** | | |
| 16 | "Option" | Dropdown | `0` |
| 17 | "Arc lead-out" | Toggle | `1` |
| 18 | "Direction" | Dropdown | `3` |
| 19 | "Cut start" | Dropdown (editable) | `1` |
| 20 | "User start" | Float | `0.0000` |
| 21 | User gcode | G-code | `` |
| 22 | "Cut down to" | Dropdown (editable) | `1` |
| 23 | "User depth" | Float | `-0.5000` |
| 24 | User depth gcode | G-code | `` |
| | **"Finishing"** | | |
| 26 | "Finishing pass" | Dropdown | `0` |
| 27 | "Finishing cut" | Float | `0.0400` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_pv`
- "Show design"

### "X"
- **NGC variable**: `#param_x`
- "Reference coord"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X axis align"
- **NGC variable**: `#param_al_x`
- "Define X reference point"
- **Options**: "Left=0:Center=1:Right=2"

### "Y"
- **NGC variable**: `#param_y`
- "Reference coord"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y axis align"
- **NGC variable**: `#param_al_y`
- "Define Y reference point"
- **Options**: "Top=0:Center=1:Bottom=2"

### "Width"
- **NGC variable**: `#param_w`
- "Positive value only"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Height"
- **NGC variable**: `#param_h`
- "Positive value only"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Rotation"
- **NGC variable**: `#param_rot`
- "Angle rotated"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Type"
- **NGC variable**: `#param_ct`
- "Select corner type"
- **Options**: "None=0:Rounded=1:Beveled=2:Inverted Round=3"

### "Radius"
- **NGC variable**: `#param_cr`
- "Radius for rounded or distance from apex"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

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
- "Usualy conventional has better finish"
- **Options**: "None=0:Clockwise=2:Clockwise full depth=12:Counter-Clockwise=3:Counter-Clockwise full depth=13"

### "Finishing cut"
- **NGC variable**: `#param_fcs`
- "Last finishing cut"
- **Min**: 0.01  **Max**: 999999.9  **Digits**: 4

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(rectangle author : Fernand Veilleux)

o<#self_id_active> if [#param_act]
	o<#self_id_00> if [#param_h GT #param_w] (if narrower than high)
		#<h#ID>   = [#param_w]
		#<w#ID>   = [#param_h]
		#<rot#ID> = [90.0 + #param_rot]
		o<select> CALL [31] [#param_al_x] [-#<h#ID> / 2] [0] [#<h#ID> / 2]
		o<select> CALL [32] [#param_al_y] [-#<w#ID> / 2] [0] [#<w#ID> / 2]

	o<#self_id_00> else
		#<w#ID>   = [#param_w]
		#<h#ID>   = [#param_h]
		#<rot#ID> = #param_rot
		o<select> CALL [32] [#param_al_x] [#<w#ID> / 2] [0] [-#<w#ID> / 2]
		o<select> CALL [31] [#param_al_y] [-#<h#ID> / 2] [0] [#<h#ID> / 2]
	o<#self_id_00> endif

	#<fcs#ID> = [#param_fcs]
	o<get_min> CALL [37] [2] [#param_cr] [#<h#ID> / 2]

	o<select> CALL [33] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [34] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<rectangle> CALL [#param_x] [#param_y] [#<w#ID>] [#<h#ID>] [#<rot#ID>] [#32] [#31] [#param_ct] [#37] [#param_opt] [#param_dir] [#33] [#34] [#param_pv] [#param_fp] [#<fcs#ID>] [#param_xa]

o<#self_id_active> endif
(end #sub_name)
```
