# "Group Offset"

>"<b>Offset and/or Rotate a Group of items</b>"

| | |
|---|---|
| Type | `group_off` |
| Icon | `group-offset.png` |
| Source | `group-off.cfg` |

## Subroutine

- **NGC**: ``

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Coords and rotation"** | | |
| 3 | "cX" | Float | `0.0000` |
| 4 | "cY" | Float | `0.0000` |
| 5 | "Rotate" | Float | `0.00` |
| | **"Items offsets"** | | |
| 7 | "dX" | Float | `0.0000` |
| 8 | "dY" | Float | `0.0000` |
| 9 | "Items" | items | `` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Disabling will disable ALL items"

### "cX"
- **NGC variable**: `#param_cx`
- "Rotation center"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "cY"
- **NGC variable**: `#param_cy`
- "Rotation center"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Rotate"
- **NGC variable**: `#param_dr`
- "Angle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "dX"
- **NGC variable**: `#param_dx`
- "X offset"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "dY"
- **NGC variable**: `#param_dy`
- "Y offset"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Items"
- **NGC variable**: `#param_0`
- "Items to group"

## G-code Template

### Before (preamble)

```ngc
(begin #sub_name)
(group offset and rotation authors : Nick Drobchenko and Fernand Veilleux)

o<#self_id_active> if [#param_act]
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
	#<angle#ID> = [#<_offsets_r> + #param_dr]

	(change coords system)
	G#<_off_rot_coord_system>

	(get rotated coordinates then apply to new coords)
	o<rotate_xy> CALL [#<cx#ID> + #param_dx] [#<cy#ID> + #param_dy] [#<cx#ID>] [#<cy#ID>] [#<angle#ID>]
	o<#self_id_change_coords> if [#<_has_z_axis>]
		G10 L2 P#5220 X#<_rotated_x> Y#<_rotated_y> Z#<offset_z#ID> R#<angle#ID>
	o<#self_id_change_coords> else
		G10 L2 P#5220 X#<_rotated_x> Y#<_rotated_y> R#<angle#ID>
	o<#self_id_change_coords> endif

	(begin #sub_name items)
```

### After (postamble)

```ngc
(end #sub_name items)

	(restore coordinate system)
	G#<old_coord_system#ID>
	G10 L2 P#5220 X#<offset_x#ID> Y#<offset_y#ID> Z#<offset_z#ID> R#<offset_r#ID>
	o<#self_id_restore_coords> if [#<_has_z_axis>]
		G10 L2 P#5220 X#<offset_x#ID> Y#<offset_y#ID> Z#<offset_z#ID> R#<offset_r#ID>
	o<#self_id_restore_coords> else
		G10 L2 P#5220 X#<offset_x#ID> Y#<offset_y#ID> R#<offset_r#ID>
	o<#self_id_restore_coords> endif

o<#self_id_active> endif
(end #sub_name)
```
