# "Drill Single"

>"<b>Drill a Single hole</b>"

| | |
|---|---|
| Type | `drill-one` |
| Icon | `drill-single.png` |
| Source | `mill/drill-single.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(drill a single hole author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND [#<_tool_usage> EQ 3]] (if active)
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<surface> + #<center_drill_depth>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<set_spindle_rpm> CALL [#<_drill_rpm>] [#<_drill_feed>]

	o<drill_single> CALL [#param_x] [#param_y] [#31] [#32] [#<drill_diameter>] [#<drill_point_len>] [#param_fcut]

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
| | **"Coords"** | | |
| 4 | "X" | Float | `0.0000` |
| 5 | "Y" | Float | `0.0000` |
| | **"Drilling"** | | |
| 7 | "Drill start" | Dropdown (editable) | `1` |
| 8 | "User start" | Float | `0.0000` |
| 9 | User gcode | G-code | `` |
| 10 | "Drill down to" | Dropdown (editable) | `1` |
| 11 | "User depth" | Float | `-0.5000` |
| 12 | User depth gcode | G-code | `` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_fcut`
- "Show design"

### "X"
- **NGC variable**: `#param_x`
- "X coordinate"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y"
- **NGC variable**: `#param_y`
- "Y coordinate"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

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
(drill a single hole author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND [#<_tool_usage> EQ 3]] (if active)
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<surface> + #<center_drill_depth>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<set_spindle_rpm> CALL [#<_drill_rpm>] [#<_drill_feed>]

	o<drill_single> CALL [#param_x] [#param_y] [#31] [#32] [#<drill_diameter>] [#<drill_point_len>] [#param_fcut]

	o<#self_id_stop> if [#<_spindle_all_time> EQ 0]
		M9 M5
	o<#self_id_stop> endif

o<#self_id_active> endif
(end #sub_name)
```
