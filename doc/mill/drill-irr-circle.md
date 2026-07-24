# "Drill Irr Circle"

>"<b>Drill Irregular Circle</b>"

| | |
|---|---|
| Type | `drill_cir_irr` |
| Icon | `drill-irr-circle.png` |
| Source | `mill/drill-circle-irr.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(drill irregular circle of #param_num holes author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND [#<_tool_usage> EQ 3]]
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#31 + #<center_drill_depth>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<set_spindle_rpm> CALL [#<_drill_rpm>] [#<_drill_feed>]

	o<#self_id_center> if [#param_center]
		o<drill_single> CALL [#param_cx] [#param_cy] [#31] [#32] [#<drill_diameter>] [#<drill_point_len>] [#param_fcut]
	o<#self_id_center> endif

	#<radius#ID> = [#param_d / 2]
	#<i#ID> = 0
	o<#self_id_loop> while [#<i#ID> LT #param_num]
		o<#self_id_i> if [#<i#ID> EQ 0]
			o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_h1]
		o<#self_id_i> elseif [#<i#ID> EQ 1]
			o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_h2]
		o<#self_id_i> elseif [#<i#ID> EQ 2]
			o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_h3]
		o<#self_id_i> elseif [#<i#ID> EQ 3]
			o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_h4]
		o<#self_id_i> elseif [#<i#ID> EQ 4]
			o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_h5]
		o<#self_id_i> else
			o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_h6]
		o<#self_id_i> endif

		o<drill_single> CALL [#param_cx + #<_rotated_x>] [#param_cy + #<_rotated_y>] [#31] [#32] [#<drill_diameter>] [#<drill_point_len>] [#param_fcut]
		#<i#ID> = [#<i#ID> + 1]
	o<#self_id_loop> endwhile

	o<#self_id_stop> if [#<_spindle_all_time> EQ 0]
		M9 M5
	o<#self_id_stop> endif

	o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords, size"** | | |
| 4 | "cX" | Float | `0.0000` |
| 5 | "cY" | Float | `0.0000` |
| 6 | "Diameter" | Float | `2.0000` |
| | **"Count, positions"** | | |
| 8 | "Number of holes" | Integer | `3` |
| 9 | "Hole 1 At" | Float | `10.00` |
| 10 | "Hole 2 At" | Float | `60.00` |
| 11 | "Hole 3 At" | Float | `120.00` |
| 12 | "Hole 4 At" | Float | `0.00` |
| 13 | "Hole 5 At" | Float | `0.00` |
| 14 | "Hole 6 At" | Float | `0.00` |
| 15 | "Drill center" | Toggle | `0` |
| | **"Drilling params"** | | |
| 17 | "Drill start" | Dropdown (editable) | `1` |
| 18 | "User start" | Float | `0.0000` |
| 19 | User gcode | G-code | `` |
| 20 | "Cut down to" | Dropdown (editable) | `1` |
| 21 | "User depth" | Float | `-0.5000` |
| 22 | User depth gcode | G-code | `` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_fcut`
- "Show design"

### "cX"
- **NGC variable**: `#param_cx`
- "Center of circle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "cY"
- **NGC variable**: `#param_cy`
- "Center of circle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Diameter"
- **NGC variable**: `#param_d`
- "Diameter of circle"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Number of holes"
- **NGC variable**: `#param_num`
- "Number of holes"

### "Hole 1 At"
- **NGC variable**: `#param_h1`
- "Angle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Hole 2 At"
- **NGC variable**: `#param_h2`
- "Angle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Hole 3 At"
- **NGC variable**: `#param_h3`
- "Angle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Hole 4 At"
- **NGC variable**: `#param_h4`
- "Angle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Hole 5 At"
- **NGC variable**: `#param_h5`
- "Angle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Hole 6 At"
- **NGC variable**: `#param_h6`
- "Angle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Drill center"
- **NGC variable**: `#param_center`
- "Drill also at center"

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

### "Cut down to"
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
(drill irregular circle of #param_num holes author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND [#<_tool_usage> EQ 3]]
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#31 + #<center_drill_depth>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<set_spindle_rpm> CALL [#<_drill_rpm>] [#<_drill_feed>]

	o<#self_id_center> if [#param_center]
		o<drill_single> CALL [#param_cx] [#param_cy] [#31] [#32] [#<drill_diameter>] [#<drill_point_len>] [#param_fcut]
	o<#self_id_center> endif

	#<radius#ID> = [#param_d / 2]
	#<i#ID> = 0
	o<#self_id_loop> while [#<i#ID> LT #param_num]
		o<#self_id_i> if [#<i#ID> EQ 0]
			o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_h1]
		o<#self_id_i> elseif [#<i#ID> EQ 1]
			o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_h2]
		o<#self_id_i> elseif [#<i#ID> EQ 2]
			o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_h3]
		o<#self_id_i> elseif [#<i#ID> EQ 3]
			o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_h4]
		o<#self_id_i> elseif [#<i#ID> EQ 4]
			o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_h5]
		o<#self_id_i> else
			o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_h6]
		o<#self_id_i> endif

		o<drill_single> CALL [#param_cx + #<_rotated_x>] [#param_cy + #<_rotated_y>] [#31] [#32] [#<drill_diameter>] [#<drill_point_len>] [#param_fcut]
		#<i#ID> = [#<i#ID> + 1]
	o<#self_id_loop> endwhile

	o<#self_id_stop> if [#<_spindle_all_time> EQ 0]
		M9 M5
	o<#self_id_stop> endif

	o<#self_id_active> endif
(end #sub_name)
```
