# "Polyline"

>"<b>Create a closed or open Polyline</b>&#10;<span foreground='blue' style='oblique'><b>Message possible in terminal window</b></span>"

| | |
|---|---|
| Type | `polyline` |
| Icon | `polyline.png` |
| Source | `mill/polyline.cfg` |

## Subroutine

- **NGC**: ``

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Origin"** | | |
| 4 | "X" | Float | `0.0000` |
| 5 | "Y" | Float | `0.0000` |
| | **"Rotation"** | | |
| 7 | "cX" | Float | `0.0000` |
| 8 | "cY" | Float | `0.0000` |
| 9 | "Rotation" | Float | `0.00` |
| | **"Offsets"** | | |
| 11 | "dX" | Float | `0.0000` |
| 12 | "dY" | Float | `0.0000` |
| | **"Milling"** | | |
| 14 | "Global tool engagement" | Integer | `100` |
| 15 | "Tool compensation" | Dropdown | `40` |
| 16 | "Direction" | Dropdown | `0` |
| 17 | "Cut start" | Dropdown (editable) | `1` |
| 18 | "User start" | Float | `0.0000` |
| 19 | User gcode | G-code | `` |
| 20 | "Cut down to" | Dropdown (editable) | `1` |
| 21 | "User depth" | Float | `-0.5000` |
| 22 | User depth gcode | G-code | `` |
| 23 | "Items" | items | `` |
| | **"Closing"** | | |
| 25 | "Closing item" | Dropdown | `0` |
| | **"Link"** | | |
| 27 | "Type" | Dropdown | `0` |
| 28 | "Radius" | Float | `0.3000` |
| 29 | "Complement" | Toggle | `0` |
| | **"Arc definition"** | | |
| 31 | "Option" | Dropdown | `0` |
| 32 | "Size" | Float | `1.0000` |
| 33 | "Flip center" | Toggle | `0` |
| | **"Milling"** | | |
| 35 | "Tool engagement" | Dropdown (editable) | `0` |
| 36 | "Tool engagement" | Integer | `100` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_fcut`
- "Show design"

### "X"
- **NGC variable**: `#param_x`
- "Origin X"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y"
- **NGC variable**: `#param_y`
- "Origin Y"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "cX"
- **NGC variable**: `#param_cx`
- "Rotation center"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "cY"
- **NGC variable**: `#param_cy`
- "Rotation center"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Rotation"
- **NGC variable**: `#param_rot`
- "Rotation around center"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "dX"
- **NGC variable**: `#param_dx`
- "Offset origin"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "dY"
- **NGC variable**: `#param_dy`
- "Offset origin"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Global tool engagement"
- **NGC variable**: `#param_gte`
- "Global tool engagement"

### "Tool compensation"
- **NGC variable**: `#param_comp`
- "Which side cutter will travel"
- **Options**: "None=40:Left=41:Right=42"

### "Direction"
- **NGC variable**: `#param_dir`
- "Mill as designed or in reverse"
- **Options**: "Designed=0:Reverse=1"

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

### "Items"
- **NGC variable**: `#param_items`
- "Add polyline items here"

### "Closing item"
- **NGC variable**: `#param_cdir`
- "Closed or not and direction of closing line"
- **Options**: "None=0:Straight line=1:Arc clockwise=2:Arc counter-clockwise=3"

### "Type"
- **NGC variable**: `#param_orcs`
- "Select link type"
- **Options**: "None=0:Rounded=1:Beveled=2:Inverted Round=3"

### "Radius"
- **NGC variable**: `#param_orcr`
- "Radius for rounded or distance from apex"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Complement"
- **NGC variable**: `#param_orrev`
- "Reverse direction of tool path for rounded or inverted round"

### "Option"
- **NGC variable**: `#param_atype`
- "Select value defined"
- **Options**: "Radius=0:Arc height=1"

### "Size"
- **NGC variable**: `#param_height`
- "Size"
- **Min**: 0  **Max**: 999999.9  **Digits**: 4

### "Flip center"
- **NGC variable**: `#param_rev2`
- "Center opposite side of chord"

### "Tool engagement"
- **NGC variable**: `#param_ted`
- "Tool engagement for this segment"
- **Options**: "Global=0:Specific=1"

### "Tool engagement"
- **NGC variable**: `#param_te`
- "Tool engagement"

## G-code Template

### Before (preamble)

```ngc
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND [#<in_polyline> EQ 0]]
	#<poly_global_engagement> = [#param_gte / 100]

	(init and set origin)
	o<poly_add_item> CALL [-1] [#param_x] [#param_y]

	#<in_polyline> = 1
	(begin #sub_name items)
```

### After (postamble)

```ngc
(end #sub_name items)
	#<in_polyline> = 0

	o<#self_id_end> if [#5000 GT 0]

		(return to origin w/ either a line 1 or an arc 5)
		o<select> CALL [31] [#param_ted] [#<poly_global_engagement>] [#param_te]
		o<#self_id_end0> if [#param_cdir GT 1]
			o<poly_add_item> CALL [5] [#param_x] [#param_y] [#param_cdir] [#param_orcs] [#param_orcr] [#param_orrev] [#31] [#param_height] [#param_atype] [#param_rev2]
		o<#self_id_end0> else
			o<poly_add_item> CALL [1] [#param_x] [#param_y] [#param_cdir] [#param_orcs] [#param_orcr] [#param_orrev] [#31]
		o<#self_id_end0> endif

		o<poly_create> CALL

		o<#self_id_rev> if [#param_dir]
			o<poly_reverse> CALL
		o<#self_id_rev> endif

		o<poly_copy_mill> CALL

		o<optimize> CALL [#<_mill_data_start>] [#param_comp] [0] [#<poly_global_engagement> * #5410 / 100]

		o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
		o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

		o<poly_mill> CALL [#<_mill_data_start>] [#31] [#32] [#param_comp] [#param_fcut] [#param_dx] [#param_dy] [#param_rot] [#<poly_global_engagement>] [#param_cx] [#param_cy]

	o<#self_id_end> endif

o<#self_id_active> endif
(end #sub_name)
```
