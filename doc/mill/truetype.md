# "TrueType"

>"<b>Engraves TrueType</b>"

| | |
|---|---|
| Type | `ttt` |
| Icon | `truetype.png` |
| Source | `mill/ttt.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(truetype engraving author : Fernand Veilleux)

o<#self_id> if [#param_ena]
	(get and save current coords system offsets)
	#<old_coord_system#ID> = [#<_coord_system> / 10]
	o<get_offsets> CALL
	#<offset_x#ID> = #<_offsets_x>
	#<offset_y#ID> = #<_offsets_y>
	#<offset_z#ID> = #<_offsets_z>
	#<offset_r#ID> = #<_offsets_r>

	(change coords system)
	G#<_off_rot_coord_system>

	(get rotated coordinates then apply to new coords)
	o<rotate_xy> CALL [#<_offsets_x> + #param_x] [#<_offsets_y> + #param_y] [#<_offsets_x>] [#<_offsets_y>] [#<_offsets_r>]
	G10 L2 P#5220 X#<_rotated_x> Y#<_rotated_y> Z#<_offsets_z> R[#<_offsets_r> + #param_rot]

	(Call engraving subroutine)
	o<#self_id_engrave> CALL [#<_z_clear>] [#param_dpt] [#<surface>] [#<_feed_vertical>] [#<_feed_normal>]

	(Restore coordinate system to origin)
	G#<old_coord_system#ID>
	G10 L2 P#5220 X#<offset_x#ID> Y#<offset_y#ID> Z#<offset_z#ID> R#<offset_r#ID>

o<#self_id> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Text" | engrave | `` |
| | **"Coords, rotation"** | | |
| 4 | "X" | Float | `0.0000` |
| 5 | "Y" | Float | `0.0000` |
| 6 | "Rotation" | Float | `0.00` |
| | **"Font"** | | |
| 8 | "Font file" | filename | `/usr/share/fonts/truetype/freefont/FreeSerifBoldItalic.ttf` |
| 9 | "Unicode" | Toggle | `0` |
| 10 | "Filled" | Toggle | `0` |
| 11 | "Filling scale" | Integer | `24` |
| | **"Format"** | | |
| 13 | "Align vertical" | Dropdown | `0` |
| 14 | "Align horizontal" | Dropdown | `0` |
| 15 | "Mirrored" | Toggle | `0` |
| 16 | "Text height" | Float | `0.5000` |
| 17 | "Stretch" | Integer | `100` |
| 18 | "Line spacing" | Float | `1.0000` |
| 19 | "Engraving depth" | Float | `-0.0100` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_ena`
- "Active"

### "Text"
- **NGC variable**: `#param_text`
- "Text"

### "X"
- **NGC variable**: `#param_x`
- "X"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y"
- **NGC variable**: `#param_y`
- "Y"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Rotation"
- **NGC variable**: `#param_rot`
- "Angle rotated"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Font file"
- **NGC variable**: `#param_font`
- "Font file"

### "Unicode"
- **NGC variable**: `#param_u`
- "Unicode"

### "Filled"
- **NGC variable**: `#param_e`
- "With horizontal lines"

### "Filling scale"
- **NGC variable**: `#param_l`
- "Filling scale"

### "Align vertical"
- **NGC variable**: `#param_va`
- "Align vertical"
- **Options**: "Bottom of first line=0:Top of first line=1:Center=2:Bottom of last line=3"

### "Align horizontal"
- **NGC variable**: `#param_ha`
- "Align horizontal"
- **Options**: "Left=0:Center=1:Right=2"

### "Mirrored"
- **NGC variable**: `#param_mode`
- "Mirrored"

### "Text height"
- **NGC variable**: `#param_th`
- "Y Size of text"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Stretch"
- **NGC variable**: `#param_st`
- "Stretch or compress"

### "Line spacing"
- **NGC variable**: `#param_ls`
- "Ratio to Text height"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Engraving depth"
- **NGC variable**: `#param_dpt`
- "Engraving depth"
- **Min**: -999999.9  **Max**: 0.0  **Digits**: 4

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(truetype engraving author : Fernand Veilleux)

o<#self_id> if [#param_ena]
	(get and save current coords system offsets)
	#<old_coord_system#ID> = [#<_coord_system> / 10]
	o<get_offsets> CALL
	#<offset_x#ID> = #<_offsets_x>
	#<offset_y#ID> = #<_offsets_y>
	#<offset_z#ID> = #<_offsets_z>
	#<offset_r#ID> = #<_offsets_r>

	(change coords system)
	G#<_off_rot_coord_system>

	(get rotated coordinates then apply to new coords)
	o<rotate_xy> CALL [#<_offsets_x> + #param_x] [#<_offsets_y> + #param_y] [#<_offsets_x>] [#<_offsets_y>] [#<_offsets_r>]
	G10 L2 P#5220 X#<_rotated_x> Y#<_rotated_y> Z#<_offsets_z> R[#<_offsets_r> + #param_rot]

	(Call engraving subroutine)
	o<#self_id_engrave> CALL [#<_z_clear>] [#param_dpt] [#<surface>] [#<_feed_vertical>] [#<_feed_normal>]

	(Restore coordinate system to origin)
	G#<old_coord_system#ID>
	G10 L2 P#5220 X#<offset_x#ID> Y#<offset_y#ID> Z#<offset_z#ID> R#<offset_r#ID>

o<#self_id> endif
(end #sub_name)
```

### Definitions

```ngc
<subprocess>python %SYS_DIR%/ttt -n#self_id -h#param_ha -v#param_va -H#param_th -f"#param_font" -i#param_ls -m#param_mode -e#param_e -l#param_l -t#param_st -u#param_u -T"0#param_text"</subprocess>
```
