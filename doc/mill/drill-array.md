# "Drill Array"

>"<b>Drill Lines of Holes</b>"

| | |
|---|---|
| Type | `drill-array` |
| Icon | `drill-array.png` |
| Source | `mill/drill-array.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(drill #param_xc by #param_yc holes author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND [#<_tool_usage> EQ 3]] (if active)
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#31 + #<center_drill_depth>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<#self_id_01> if [#param_xc EQ 1]
		#33 = 0
	o<#self_id_01> else
		o<select> CALL [33] [#param_dxdef] [#param_dx] [#param_dx / [#param_xc - 1]]
	o<#self_id_01> endif
	#<dx#ID> = #33
	o<select> CALL [33] [#param_al_x] [0] [- [#param_xc - 1] * #<dx#ID> / 2] [- [#param_xc - 1] * #<dx#ID>]
	#<first_x#ID> = #33

	o<#self_id_02> if [#param_yc EQ 1]
		#33 = 0
	o<#self_id_02> else
		o<select> CALL [33] [#param_dydef] [#param_dy] [#param_dy / [#param_yc - 1]]
	o<#self_id_02> endif
	#<dy#ID> = #33
	o<select> CALL [33] [#param_al_y] [- #<dy#ID> * [#param_yc - 1]] [- #<dy#ID> * [#param_yc - 1] / 2] [0]
	#<first_y#ID> = #33

	(get and save current coords system offsets)
	#<old_coord_system#ID> = [#<_coord_system> / 10]
	o<get_offsets> CALL
	#<offset_x#ID> = #<_offsets_x>
	#<offset_y#ID> = #<_offsets_y>
	#<offset_z#ID> = #<_offsets_z>
	#<offset_r#ID> = #<_offsets_r>

	(change coords system)
	G#<_off_rot_coord_system>

	o<set_spindle_rpm> CALL [#<_drill_rpm>] [#<_drill_feed>]
	#<start_y#ID> = [#<offset_y#ID> + #<first_y#ID>]
	#<x_step#ID>  = 1
	#<x_round#ID> = 0
	#<start_x#ID> = [#<offset_x#ID> + #<first_x#ID>]

	o<#self_id_loop_Y> repeat [#param_yc]
		o<#self_id_loop_X> repeat [#param_xc]
			(get rotated coordinates then apply to new coords)
			o<rotate_xy> CALL [#<start_x#ID> + #param_x] [#<start_y#ID> + #param_y] [#<offset_x#ID> + #param_x] [#<offset_y#ID> + #param_y] [#<offset_r#ID> + #param_rot]
			G10 L2 P#5220 X[#<_rotated_x>] Y[#<_rotated_y>] Z#<offset_z#ID> R[#<offset_r#ID> + #param_rot]

			o<drill_single> CALL [0] [0] [#31] [#32] [#<drill_diameter>] [#<drill_point_len>] [#param_fcut]

			#<x_round#ID> = [#<x_round#ID> + #<x_step#ID>]
			o<#self_id_inc> if [[#<x_round#ID> LT #param_xc] AND [#<x_round#ID> GT 0]]
				#<start_x#ID>  = [#<start_x#ID>  + #<dx#ID> * #<x_step#ID>]
			o<#self_id_inc> endif
		o<#self_id_loop_X> endrepeat

		#<x_step#ID>  = [#<x_step#ID>   * -1]
		#<start_y#ID> = [#<start_y#ID> + #<dy#ID>]
	o<#self_id_loop_Y> endrepeat

	o<#self_id_stop> if [#<_spindle_all_time> EQ 0]
		M9 M5
	o<#self_id_stop> endif

	(restore coordinate system)
	G#<old_coord_system#ID>
	G10 L2 P#5220 X#<offset_x#ID> Y#<offset_y#ID> Z#<offset_z#ID> R#<offset_r#ID>

o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords"** | | |
| 4 | "X" | Float | `0.0000` |
| 5 | "Align axis" | Dropdown | `1` |
| 6 | "Y" | Float | `0.0000` |
| 7 | "Align axis" | Dropdown | `1` |
| | **"Size and offsets"** | | |
| 9 | "X axis count" | Integer | `2` |
| 10 | "dX" | Float | `1.0000` |
| 11 | "dX options" | Dropdown | `0` |
| 12 | "Y axis count" | Integer | `2` |
| 13 | "dY" | Float | `0.5000` |
| 14 | "dY options" | Dropdown | `0` |
| | **"Rotation"** | | |
| 16 | "Angle" | Float | `0.00` |
| | **"Drilling"** | | |
| 18 | "Drill start" | Dropdown (editable) | `1` |
| 19 | "User start" | Float | `0.0000` |
| 20 | User gcode | G-code | `` |
| 21 | "Drill down to" | Dropdown (editable) | `1` |
| 22 | "User depth" | Float | `0.0000` |
| 23 | User depth gcode | G-code | `` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_fcut`
- "Show design"

### "X"
- **NGC variable**: `#param_x`
- "X reference"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Align axis"
- **NGC variable**: `#param_al_x`
- "Define X reference point"
- **Options**: "Left=0:Center=1:Right=2"

### "Y"
- **NGC variable**: `#param_y`
- "Y reference"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Align axis"
- **NGC variable**: `#param_al_y`
- "Define Y reference point"
- **Options**: "Top=0:Center=1:Bottom=2"

### "X axis count"
- **NGC variable**: `#param_xc`
- "Number of holes"

### "dX"
- **NGC variable**: `#param_dx`
- "X offset"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "dX options"
- **NGC variable**: `#param_dxdef`
- "Define dX"
- **Options**: "Between each hole=0:Overall=1"

### "Y axis count"
- **NGC variable**: `#param_yc`
- "Number of holes"

### "dY"
- **NGC variable**: `#param_dy`
- "Y offset"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "dY options"
- **NGC variable**: `#param_dydef`
- "Define dY"
- **Options**: "Between each hole=0:Overall=1"

### "Angle"
- **NGC variable**: `#param_rot`
- "Rotation of line"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Drill start"
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

### "Drill down to"
- **NGC variable**: `#param_dpt`
- "Pre or user defined"
- **Options**: "User defined=0:Through=1:Center drill depth=2:Bottom=3:Half=4:One quarter=5:Three quarter=6:G-Code=7"

### "User depth"
- **NGC variable**: `#param_u_dpt`
- "User depth"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### User depth gcode
- **NGC variable**: `#param_ugcd`
- User depth gcode

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(drill #param_xc by #param_yc holes author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND [#<_tool_usage> EQ 3]] (if active)
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#31 + #<center_drill_depth>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<#self_id_01> if [#param_xc EQ 1]
		#33 = 0
	o<#self_id_01> else
		o<select> CALL [33] [#param_dxdef] [#param_dx] [#param_dx / [#param_xc - 1]]
	o<#self_id_01> endif
	#<dx#ID> = #33
	o<select> CALL [33] [#param_al_x] [0] [- [#param_xc - 1] * #<dx#ID> / 2] [- [#param_xc - 1] * #<dx#ID>]
	#<first_x#ID> = #33

	o<#self_id_02> if [#param_yc EQ 1]
		#33 = 0
	o<#self_id_02> else
		o<select> CALL [33] [#param_dydef] [#param_dy] [#param_dy / [#param_yc - 1]]
	o<#self_id_02> endif
	#<dy#ID> = #33
	o<select> CALL [33] [#param_al_y] [- #<dy#ID> * [#param_yc - 1]] [- #<dy#ID> * [#param_yc - 1] / 2] [0]
	#<first_y#ID> = #33

	(get and save current coords system offsets)
	#<old_coord_system#ID> = [#<_coord_system> / 10]
	o<get_offsets> CALL
	#<offset_x#ID> = #<_offsets_x>
	#<offset_y#ID> = #<_offsets_y>
	#<offset_z#ID> = #<_offsets_z>
	#<offset_r#ID> = #<_offsets_r>

	(change coords system)
	G#<_off_rot_coord_system>

	o<set_spindle_rpm> CALL [#<_drill_rpm>] [#<_drill_feed>]
	#<start_y#ID> = [#<offset_y#ID> + #<first_y#ID>]
	#<x_step#ID>  = 1
	#<x_round#ID> = 0
	#<start_x#ID> = [#<offset_x#ID> + #<first_x#ID>]

	o<#self_id_loop_Y> repeat [#param_yc]
		o<#self_id_loop_X> repeat [#param_xc]
			(get rotated coordinates then apply to new coords)
			o<rotate_xy> CALL [#<start_x#ID> + #param_x] [#<start_y#ID> + #param_y] [#<offset_x#ID> + #param_x] [#<offset_y#ID> + #param_y] [#<offset_r#ID> + #param_rot]
			G10 L2 P#5220 X[#<_rotated_x>] Y[#<_rotated_y>] Z#<offset_z#ID> R[#<offset_r#ID> + #param_rot]

			o<drill_single> CALL [0] [0] [#31] [#32] [#<drill_diameter>] [#<drill_point_len>] [#param_fcut]

			#<x_round#ID> = [#<x_round#ID> + #<x_step#ID>]
			o<#self_id_inc> if [[#<x_round#ID> LT #param_xc] AND [#<x_round#ID> GT 0]]
				#<start_x#ID>  = [#<start_x#ID>  + #<dx#ID> * #<x_step#ID>]
			o<#self_id_inc> endif
		o<#self_id_loop_X> endrepeat

		#<x_step#ID>  = [#<x_step#ID>   * -1]
		#<start_y#ID> = [#<start_y#ID> + #<dy#ID>]
	o<#self_id_loop_Y> endrepeat

	o<#self_id_stop> if [#<_spindle_all_time> EQ 0]
		M9 M5
	o<#self_id_stop> endif

	(restore coordinate system)
	G#<old_coord_system#ID>
	G10 L2 P#5220 X#<offset_x#ID> Y#<offset_y#ID> Z#<offset_z#ID> R#<offset_r#ID>

o<#self_id_active> endif
(end #sub_name)
```
