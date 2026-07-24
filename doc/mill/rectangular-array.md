# "Rectangular Array"

>"<b>Create a Rectangular Array of items</b>"

| | |
|---|---|
| Type | `rect-array` |
| Icon | `rect-array.png` |
| Source | `rectangular-array.cfg` |

## Subroutine

- **NGC**: ``

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Coords"** | | |
| 3 | "X" | Float | `0.0000` |
| 4 | "X axis align" | Dropdown | `0` |
| 5 | "Y" | Float | `0.0000` |
| 6 | "Y axis align" | Dropdown | `2` |
| 7 | "Z" | Float | `0.0000` |
| | **"Size and offsets"** | | |
| 9 | "X axis copies" | Integer | `2` |
| 10 | "dX" | Float | `1.0000` |
| 11 | "Y axis copies" | Integer | `3` |
| 12 | "dY" | Float | `1.0000` |
| | **"Rotation"** | | |
| 14 | "Array rotation" | Float | `0.00` |
| 15 | "X items rotation" | Float | `0.00` |
| 16 | "Y items rotation" | Float | `0.00` |
| 17 | "Items" | items | `` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Disabling will disable ALL items"

### "X"
- **NGC variable**: `#param_x`
- "Origin X"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X axis align"
- **NGC variable**: `#param_alx`
- "Define X reference"
- **Options**: "Left=0:Center=1:Right=2"

### "Y"
- **NGC variable**: `#param_y`
- "Origin Y"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y axis align"
- **NGC variable**: `#param_aly`
- "Define Y reference"
- **Options**: "Top=0:Center=1:Bottom=2"

### "Z"
- **NGC variable**: `#param_z`
- "Z"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X axis copies"
- **NGC variable**: `#param_numx`
- "Number of copies"

### "dX"
- **NGC variable**: `#param_dx`
- "X step"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y axis copies"
- **NGC variable**: `#param_numy`
- "Number of copies"

### "dY"
- **NGC variable**: `#param_dy`
- "Y step"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Array rotation"
- **NGC variable**: `#param_r`
- "Rotation of array"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "X items rotation"
- **NGC variable**: `#param_xr`
- "Relative to previous one"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Y items rotation"
- **NGC variable**: `#param_yr`
- "Relative to previous one"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Items"
- **NGC variable**: `#param_items`
- "Items to copy"

## G-code Template

### Before (preamble)

```ngc
(begin #sub_name)
(rectangular array author : Fernand Veilleux)

o<#self_id_active> if [#param_act]
	o<select> CALL [31] [#param_alx] [#param_x] [#param_x - [#param_numx - 1] * #param_dx / 2] [#param_x - [#param_numx - 1] * #param_dx]
	#<first_x#ID> = #31

	o<select> CALL [31] [#param_aly] [#param_y - [#param_numy - 1] * #param_dy] [#param_y - [#param_numy - 1] * #param_dy / 2] [#param_y]
	#<first_y#ID> = #31

	(get and save current coords system offsets)
	#<old_coord_system#ID> = [#<_coord_system> / 10]
	o<get_offsets> CALL
	#<offset_x#ID> = #<_offsets_x>
	#<offset_y#ID> = #<_offsets_y>
	#<offset_z#ID> = #<_offsets_z>
	#<offset_r#ID> = #<_offsets_r>

	(change coords system)
	G#<_off_rot_coord_system>

	#<start_y#ID>  = [#<offset_y#ID> + #<first_y#ID>]
	#<items_yr#ID> = 0
	#<x_step#ID>   = 1
	#<x_round#ID>  = 0
	#<start_x#ID>  = [#<offset_x#ID> + #<first_x#ID>]
	#<items_xr#ID> = 0
	o<#self_id_loop_Y> repeat [#param_numy]
		o<#self_id_loop_X> repeat [#param_numx]
			(get rotated coordinates then apply to new coords)
			#<rot#ID> = [#<offset_r#ID> + #param_r + #<items_xr#ID> + #<items_yr#ID>]
			o<rotate_xy> CALL [#<start_x#ID>] [#<start_y#ID>] [#<offset_x#ID> + #param_x] [#<offset_y#ID> + #param_y] [#<offset_r#ID> + #param_r]
			o<#self_id_change_coords> if [#<_has_z_axis>]
				G10 L2 P#5220 X[#<_rotated_x>] Y[#<_rotated_y>] Z#<offset_z#ID> R[#<rot#ID>]
			o<#self_id_change_coords> else
				G10 L2 P#5220 X[#<_rotated_x>] Y[#<_rotated_y>] R[#<rot#ID>]
			o<#self_id_change_coords> endif

			(begin #sub_name items)
```

### After (postamble)

```ngc
(end #sub_name items)

			#<x_round#ID> = [#<x_round#ID> + #<x_step#ID>]
			o<#self_id_inc> if [[#<x_round#ID> LT #param_numx] AND [#<x_round#ID> GT 0]]
				#<start_x#ID>  = [#<start_x#ID>  + #param_dx * #<x_step#ID>]
				#<items_xr#ID> = [#<items_xr#ID> + #param_xr * #<x_step#ID>]
			o<#self_id_inc> endif
		o<#self_id_loop_X> endrepeat

		#<x_step#ID>   = [#<x_step#ID>   * -1]
		#<start_y#ID>  = [#<start_y#ID>  + #param_dy]
		#<items_yr#ID> = [#<items_yr#ID> + #param_yr]
	o<#self_id_loop_Y> endrepeat

	(restore coordinate system)
	G#<old_coord_system#ID>
	o<#self_id_restore_coords> if [#<_has_z_axis>]
		G10 L2 P#5220 X#<offset_x#ID> Y#<offset_y#ID> Z#<offset_z#ID> R#<offset_r#ID>
	o<#self_id_restore_coords> else
		G10 L2 P#5220 X#<offset_x#ID> Y#<offset_y#ID> R#<offset_r#ID>
	o<#self_id_restore_coords> endif

o<#self_id_active> endif
(end #sub_name)
```
