# "Drill Circle"

>"<b>Drill a Regular Circle</b>"

| | |
|---|---|
| Type | `drill_cir` |
| Icon | `drill-circle.png` |
| Source | `mill/drill-circle.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(drill a regular circle of #param_num holes author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND [#<_tool_usage> EQ 3]]
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#31 + #<center_drill_depth>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	#<d#ID> = [#param_dim]
	o<#self_id_10> if [#param_opt] ; option diameter
		#<radius#ID> = [#<d#ID> / 2]
	o<#self_id_10> else ; option distance between holes
		o<#self_id_10a> if [[#param_ext MOD 360] EQ 0]
			#<radius#ID> = [#<d#ID> / 2 / SIN[180 / #param_num]]
		o<#self_id_10a> else
			#<radius#ID> = [#<d#ID> / SIN[#param_ext / #param_num]]
		o<#self_id_10a> endif
	o<#self_id_10> endif

	o<#self_id_20> if [[[#param_ext MOD 360] NE 0] AND [#param_num GT 1]]
		#<fill#ID> = [#param_ext * #param_num / [#param_num - 1]]
	o<#self_id_20> else
		#<fill#ID> = #param_ext
	o<#self_id_20> endif

	o<set_spindle_rpm> CALL [#<_drill_rpm>] [#<_drill_feed>]

	o<#self_id_center> if [#param_center]
		o<drill_single> CALL [#param_cx] [#param_cy] [#31] [#32] [#<drill_diameter>] [#<drill_point_len>] [#param_fcut]
	o<#self_id_center> endif

	#<i#ID> = 0
	o<#self_id_loop> while [#<i#ID> LT #param_num]
		o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_a + [#<fill#ID> / #param_num] * #<i#ID>]
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
| 6 | "Measure by" | Dropdown | `1` |
| 7 | "Dimension" | Float | `2.0000` |
| | **"Count, start, end"** | | |
| 9 | "Number of holes" | Integer | `5` |
| 10 | "Start" | Float | `0.00` |
| 11 | "Extend" | Float | `360.00` |
| 12 | "Drill center" | Toggle | `0` |
| | **"Drilling"** | | |
| 14 | "Drill start" | Dropdown | `1` |
| 15 | "User start" | Float | `0.0000` |
| 16 | User gcode | G-code | `` |
| 17 | "Drill down to" | Dropdown (editable) | `1` |
| 18 | "User depth" | Float | `-0.5000` |
| 19 | User depth gcode | G-code | `` |

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

### "Measure by"
- **NGC variable**: `#param_opt`
- "Select dimension option"
- **Options**: "Diameter=1:Distance between holes=0"

### "Dimension"
- **NGC variable**: `#param_dim`
- "Diameter or distance"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Number of holes"
- **NGC variable**: `#param_num`
- "Number of holes"

### "Start"
- **NGC variable**: `#param_a`
- "Angle of the first hole"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Extend"
- **NGC variable**: `#param_ext`
- "Angle covered by holes"
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
(drill a regular circle of #param_num holes author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND [#<_tool_usage> EQ 3]]
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#31 + #<center_drill_depth>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	#<d#ID> = [#param_dim]
	o<#self_id_10> if [#param_opt] ; option diameter
		#<radius#ID> = [#<d#ID> / 2]
	o<#self_id_10> else ; option distance between holes
		o<#self_id_10a> if [[#param_ext MOD 360] EQ 0]
			#<radius#ID> = [#<d#ID> / 2 / SIN[180 / #param_num]]
		o<#self_id_10a> else
			#<radius#ID> = [#<d#ID> / SIN[#param_ext / #param_num]]
		o<#self_id_10a> endif
	o<#self_id_10> endif

	o<#self_id_20> if [[[#param_ext MOD 360] NE 0] AND [#param_num GT 1]]
		#<fill#ID> = [#param_ext * #param_num / [#param_num - 1]]
	o<#self_id_20> else
		#<fill#ID> = #param_ext
	o<#self_id_20> endif

	o<set_spindle_rpm> CALL [#<_drill_rpm>] [#<_drill_feed>]

	o<#self_id_center> if [#param_center]
		o<drill_single> CALL [#param_cx] [#param_cy] [#31] [#32] [#<drill_diameter>] [#<drill_point_len>] [#param_fcut]
	o<#self_id_center> endif

	#<i#ID> = 0
	o<#self_id_loop> while [#<i#ID> LT #param_num]
		o<rotate_xy> CALL [#<radius#ID>] [0] [0] [0] [#param_a + [#<fill#ID> / #param_num] * #<i#ID>]
		o<drill_single> CALL [#param_cx + #<_rotated_x>] [#param_cy + #<_rotated_y>] [#31] [#32] [#<drill_diameter>] [#<drill_point_len>] [#param_fcut]
		#<i#ID> = [#<i#ID> + 1]
	o<#self_id_loop> endwhile

	o<#self_id_stop> if [#<_spindle_all_time> EQ 0]
		M9 M5
	o<#self_id_stop> endif

o<#self_id_active> endif
(end #sub_name)
```
