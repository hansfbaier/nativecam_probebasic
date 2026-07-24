# "Polyline"

>"<b>Create a closed or open Polyline</b>&#10;<span foreground='blue' style='oblique'><b>Message possible in terminal window</b></span>"

| | |
|---|---|
| Type | `polyline` |
| Icon | `polyline.png` |
| Source | `plasma/polyline.cfg` |

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
| | **"Offsets, rotation"** | | |
| 7 | "dX" | Float | `0.0000` |
| 8 | "dY" | Float | `0.0000` |
| 9 | "Rotation" | Float | `0.00` |
| | **"Cutting"** | | |
| 11 | "Kerf width compensation" | Dropdown | `40` |
| 12 | "Direction" | Dropdown | `0` |
| 13 | "Items" | items | `` |
| | **"Closing"** | | |
| 15 | "Closing item" | Dropdown | `0` |
| | **"Link"** | | |
| 17 | "Type" | Dropdown | `0` |
| 18 | "Radius" | Float | `0.3000` |
| 19 | "Complement" | Toggle | `0` |
| | **"Arc definition"** | | |
| 21 | "Option" | Dropdown | `0` |
| 22 | "Size" | Float | `1.0000` |
| 23 | "Flip center" | Toggle | `0` |

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

### "dX"
- **NGC variable**: `#param_dx`
- "Offset origin"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "dY"
- **NGC variable**: `#param_dy`
- "Offset origin"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Rotation"
- **NGC variable**: `#param_rot`
- "Rotation around offsets"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Kerf width compensation"
- **NGC variable**: `#param_comp`
- "Which side torch will travel"
- **Options**: "None=40:Left=41:Right=42"

### "Direction"
- **NGC variable**: `#param_dir`
- "Cut as designed or in reverse"
- **Options**: "Designed=0:Reverse=1"

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

## G-code Template

### Before (preamble)

```ngc
(begin #sub_name)
(polyline author : Fernand Veilleux)
o<#self_id_active> if [#param_act AND [#<in_polyline> EQ 0]]
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
		o<#self_id_end0> if [#param_cdir GT 1]
			o<poly_add_item> CALL [5] [#param_x] [#param_y] [#param_cdir] [#param_orcs] [#param_orcr] [#param_orrev] [100] [#param_height] [#param_atype] [#param_rev2]
		o<#self_id_end0> else
			o<poly_add_item> CALL [1] [#param_x] [#param_y] [#param_cdir] [#param_orcs] [#param_orcr] [#param_orrev] [100]
		o<#self_id_end0> endif

		o<poly_create> CALL

		o<#self_id_rev> if [#param_dir]
			o<poly_reverse> CALL
		o<#self_id_rev> endif

		o<poly_copy_cut> CALL

		o<poly_cut> CALL [#<_mill_data_start>] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_comp] [#param_fcut] [#param_dx] [#param_dy] [#param_rot]

	o<#self_id_end> endif
o<#self_id_active> endif
(end #sub_name)
```
