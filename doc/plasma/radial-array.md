# "Radial Array"

>"<b>Create a Radial Array of items</b>"

| | |
|---|---|
| Type | `circ-array` |
| Icon | `circular-array.png` |
| Source | `circular-array.cfg` |

## Subroutine

- **NGC**: ``

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Coords, size"** | | |
| 3 | "cX" | Float | `0.0000` |
| 4 | "cY" | Float | `0.0000` |
| 5 | "Number of copies" | Integer | `6` |
| 6 | "Size" | Float | `2.0000` |
| 7 | "Dimension is" | Dropdown | `1` |
| | **"Rotation and ends"** | | |
| 9 | "Start" | Float | `0.00` |
| 10 | "Fill angle" | Float | `360.00` |
| 11 | "Rotate items" | Toggle | `1` |
| 12 | "Items" | items | `` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Disabling will disable ALL items"

### "cX"
- **NGC variable**: `#param_cx`
- "Array center"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "cY"
- **NGC variable**: `#param_cy`
- "Array center"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Number of copies"
- **NGC variable**: `#param_num`
- "Number of copies"

### "Size"
- **NGC variable**: `#param_d`
- "Diameter of array or distance between group of items"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Dimension is"
- **NGC variable**: `#param_opt`
- "Select what dimension means"
- **Options**: "Radius=0:Diameter=1:Distance between groups=2"

### "Start"
- **NGC variable**: `#param_ang`
- "Angle of the first item"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Fill angle"
- **NGC variable**: `#param_fill`
- "Angle covered by items"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Rotate items"
- **NGC variable**: `#param_rot`
- "Rotate each group of items"

### "Items"
- **NGC variable**: `#param_items`
- "Items to copy"

## G-code Template

### Before (preamble)

```ngc
(begin #sub_name)
(radial array authors : Nick Drobchenko and Fernand Veilleux)

o<#self_id_active> if [#param_act]
	(calc radius)
	o<#self_id_option> if [#param_opt EQ 0] (distance is radius)
		#<radius#ID> = [#param_d]
	o<#self_id_option> elseif [#param_opt EQ 1] (distance is diameter)
		#<radius#ID> = [#param_d / 2]
	o<#self_id_option> else (distance is between groups of items)
		o<#self_id_optiona> if [[#param_fill MOD 360] EQ 0]
			#<radius#ID> = [#param_d / 2 / SIN[180 / #param_num]]
		o<#self_id_optiona> else
			#<radius#ID> = [#param_d / SIN[#param_fill / #param_num]]
		o<#self_id_optiona> endif
	o<#self_id_option> endif

	o<#self_id_fill> if [[[#param_fill MOD 360] NE 0] AND [#param_num GT 1]]
		#<fill#ID> = [#param_fill * #param_num / [#param_num - 1]]
	o<#self_id_fill> else
		#<fill#ID> = #param_fill
	o<#self_id_fill> endif

	(get and save current coords system offsets)
	#<old_coord_system#ID> = [#<_coord_system> / 10]
	o<get_offsets> CALL
	#<offset_x#ID> = #<_offsets_x>
	#<offset_y#ID> = #<_offsets_y>
	#<offset_z#ID> = #<_offsets_z>
	#<offset_r#ID> = #<_offsets_r>

	(calc new offsets)
	#<cx#ID>    = [#<_offsets_x> + #param_cx]
	#<cy#ID>    = [#<_offsets_y> + #param_cy]
	#<angle#ID> = [#<_offsets_r> + #param_ang]

	(change coords system)
	G#<_off_rot_coord_system>

	o<#self_id_loop> repeat [#param_num]
		(get rotated coordinates then apply to new coords)
		o<rotate_xy> CALL [#<cx#ID> + #<radius#ID>] [#<cy#ID>] [#<cx#ID>] [#<cy#ID>] [#<angle#ID>]

		o<#self_id_change_coords> if [#<_has_z_axis>]
			o<#self_id_rotate_choice> if [#param_rot] (enable rotations of items)
				G10 L2 P#5220 X#<_rotated_x> Y#<_rotated_y> Z#<offset_z#ID> R#<angle#ID>
			o<#self_id_rotate_choice> else
				G10 L2 P#5220 X#<_rotated_x> Y#<_rotated_y> Z#<offset_z#ID> R#<offset_r#ID>
			o<#self_id_rotate_choice> endif
		o<#self_id_change_coords> else
			o<#self_id_rotate_choice0> if [#param_rot] (enable rotations of items)
				G10 L2 P#5220 X#<_rotated_x> Y#<_rotated_y> R#<angle#ID>
			o<#self_id_rotate_choice0> else
				G10 L2 P#5220 X#<_rotated_x> Y#<_rotated_y> R#<offset_r#ID>
			o<#self_id_rotate_choice0> endif
		o<#self_id_change_coords> endif

		(begin #sub_name items)
```

### After (postamble)

```ngc
(end #sub_name items)

		(angular increment)
		#<angle#ID>  = [#<angle#ID> + #<fill#ID> / #param_num]
	o<#self_id_loop> endrepeat

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
