# "Rectangle"

>"<b>Create a Rectangle and align X and Y</b>&#10;Corners can be radiused or beveled"

| | |
|---|---|
| Type | `rectangle` |
| Icon | `center-rect.png` |
| Source | `plasma/rectangle.cfg` |

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

	o<get_min> CALL [37] [2] [#param_cr] [#<h#ID> / 2]

	o<rectangle> CALL [#param_x] [#param_y] [#<w#ID>] [#<h#ID>] [#<rot#ID>] [#32] [#31] [#param_ct] [#37] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_pv]
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
| | **"Cutting"** | | |
| 16 | "Option" | Dropdown | `0` |
| 17 | "Direction" | Dropdown | `3` |

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
- **Options**: "Inside=0:On the line=2:Outside=3"

### "Direction"
- **NGC variable**: `#param_dir`
- "Direction of path"
- **Options**: "Clockwise=2:Counter-Clockwise=3"

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

	o<get_min> CALL [37] [2] [#param_cr] [#<h#ID> / 2]

	o<rectangle> CALL [#param_x] [#param_y] [#<w#ID>] [#<h#ID>] [#<rot#ID>] [#32] [#31] [#param_ct] [#37] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_pv]
o<#self_id_active> endif
(end #sub_name)
```
