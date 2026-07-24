# "Facing"

>"<b>Surface Finishing</b>"

| | |
|---|---|
| Type | `surf_finish` |
| Icon | `rect-pocket.png` |
| Source | `mill/surf_finish.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(surface finishing author : Fernand Veilleux)

o<#self_id_active> if [#param_act]
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>]
	#<dnum#ID> = #5400
	#<exists#ID> = EXISTS[#<_spindle_dir>]
	o<#self_id01> if [#<exists#ID>]
		#<spindle_dir#ID>      = #<_spindle_dir>
		#<cooling_mode#ID>     = #<_cooling_mode>
		#<feed_normal#ID>      = #<_feed_normal>
		#<rpm_normal#ID>       = #<_rpm_normal>
		#<feed_vertical#ID>    = #<_feed_vertical>
		#<penetration_mode#ID> = #<_penetration_mode>
		#<depth_step#ID>       = #<_depth_step>
		#<tool_usage#ID>       = #<_tool_usage>
		#<stepover_normal#ID>  = #<_stepover_normal>
		#<tool_dynamic_dia#ID> = #<_tool_dynamic_dia>
	o<#self_id01> else
		o<select> CALL [32] [#<_metric>] [0.015] [0.4]
		#<_stepover_min> = #32
	o<#self_id01> endif
	#<_spindle_dir>      =  #param_spindle_dir
	#<_cooling_mode>     =  #param_cooling
	#<_feed_normal>      =  #param_feed
	#<_rpm_normal>       =  #param_speed
	#<_feed_vertical>    =  [#<_feed_normal> / 2]
	#<_penetration_mode> =  1
	#<_depth_step>       =  #param_stp
	#<_tool_usage>       =  0
	#<_stepover_normal>  = [#param_so / 100]
	#<_tool_dynamic_dia> =  0

	o<#self_id_tlc> if [[#param_tlc EQ 3] AND [#param_dnum GT 0]]
		M61 Q#param_dnum
	o<#self_id_tlc> endif

	o<#self_id_act> if [#param_act AND [#param_dnum NE #5400]]
		M9
		T#param_dnum M6
	o<#self_id_act> endif

	o<#self_id_lc> if [[#param_tlc EQ 1] OR [#param_tlc EQ 2]]
		G43 H#param_dnum
	o<#self_id_lc> endif

	o<#self_id_01> if [[#<_spindle_dir> GT 0] AND #<_spindle_all_time>]
		o<set_feed_rate_and_speed> CALL [1]
	o<#self_id_01> endif

	o<surf_finish> CALL [#<wp_left>] [#<wp_right>] [#<wp_front>] [#<wp_rear>] [#param_dir] [#param_mode + #param_entry] [#31] [#31 + #param_d] [#param_tc / 100] [#param_lst] [#param_touch]

	o<#self_id02> if [#<exists#ID>]
		#<_spindle_dir>      = #<spindle_dir#ID>
		#<_cooling_mode>     = #<cooling_mode#ID>
		#<_feed_normal>      = #<feed_normal#ID>
		#<_rpm_normal>       = #<rpm_normal#ID>
		#<_feed_vertical>    = #<feed_vertical#ID>
		#<_penetration_mode> = #<penetration_mode#ID>
		#<_depth_step>       = #<depth_step#ID>
		#<_tool_usage>       = #<tool_usage#ID>
		#<_stepover_normal>  = #<stepover_normal#ID>
		#<_tool_dynamic_dia> = #<tool_dynamic_dia#ID>
	o<#self_id02> endif

o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Select end mill"** | | |
| 3 | "Tool number" | tool | `0` |
| | **"Action"** | | |
| 5 | "Use length comp" | Dropdown | `3` |
| 6 | "Start spindle" | Dropdown | `3` |
| 7 | "Use cooling" | Dropdown | `8` |
| | **"Feed and speed"** | | |
| 9 | "Feed" | Float | `10.0000` |
| 10 | "Spindle speed" | Integer | `5000` |
| | **"Tool path"** | | |
| 12 | "Axis" | Dropdown | `0` |
| 13 | "Mode" | Dropdown | `0` |
| 14 | "Step over" | Integer | `60` |
| 15 | "Entry mode" | Dropdown | `0` |
| 16 | "Safety margin" | Integer | `50` |
| | **"Params"** | | |
| 18 | "Cut start" | Dropdown (editable) | `1` |
| 19 | "User start" | Float | `0.0000` |
| 20 | "Cut down to" | Float | `-0.0400` |
| 21 | "Step down" | Float | `-0.0200` |
| 22 | "Last cut" | Float | `-0.0050` |
| 23 | "Touch off Z axis" | Toggle | `1` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Tool number"
- **NGC variable**: `#param_dnum`
- "Select from tool table"

### "Use length comp"
- **NGC variable**: `#param_tlc`
- "Use G43 and probe if setup"
- **Options**: "No=0:Already mounted and touched=3:From tool table=1:Table and probe=2"

### "Start spindle"
- **NGC variable**: `#param_spindle_dir`
- "Select drill rotation"
- **Options**: "No=0:Clockwise=3:Counter-clockwise=4"

### "Use cooling"
- **NGC variable**: `#param_cooling`
- "Use flood, mist or none"
- **Options**: "None=9:Flood=8:Mist=7"

### "Feed"
- **NGC variable**: `#param_feed`
- "Feed at 100% engagement"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Spindle speed"
- **NGC variable**: `#param_speed`
- "Set spindle speed"

### "Axis"
- **NGC variable**: `#param_dir`
- "Main axis"
- **Options**: "X axis=0:Y axis=1"

### "Mode"
- **NGC variable**: `#param_mode`
- "Defines quality of finish"
- **Options**: "Bidirectional=0:Unidirectional=2"

### "Step over"
- **NGC variable**: `#param_so`
- "Maximum"

### "Entry mode"
- **NGC variable**: `#param_entry`
- "Defines quality of finish"
- **Options**: "Arc=0:Straight=1"

### "Safety margin"
- **NGC variable**: `#param_tc`
- "Percent of tool diameter past edge"

### "Cut start"
- **NGC variable**: `#param_s`
- "Pre or user defined"
- **Options**: "User defined=0:Surface=1"

### "User start"
- **NGC variable**: `#param_u_s`
- "User start"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Cut down to"
- **NGC variable**: `#param_d`
- "Relative to start"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Step down"
- **NGC variable**: `#param_stp`
- "Step down on each pass"
- **Min**: -999999.9  **Max**: 0.0  **Digits**: 4

### "Last cut"
- **NGC variable**: `#param_lst`
- "Last cut depth"
- **Min**: -999999.9  **Max**: 0.0  **Digits**: 4

### "Touch off Z axis"
- **NGC variable**: `#param_touch`
- "Set finished surface as new 0"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(surface finishing author : Fernand Veilleux)

o<#self_id_active> if [#param_act]
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>]
	#<dnum#ID> = #5400
	#<exists#ID> = EXISTS[#<_spindle_dir>]
	o<#self_id01> if [#<exists#ID>]
		#<spindle_dir#ID>      = #<_spindle_dir>
		#<cooling_mode#ID>     = #<_cooling_mode>
		#<feed_normal#ID>      = #<_feed_normal>
		#<rpm_normal#ID>       = #<_rpm_normal>
		#<feed_vertical#ID>    = #<_feed_vertical>
		#<penetration_mode#ID> = #<_penetration_mode>
		#<depth_step#ID>       = #<_depth_step>
		#<tool_usage#ID>       = #<_tool_usage>
		#<stepover_normal#ID>  = #<_stepover_normal>
		#<tool_dynamic_dia#ID> = #<_tool_dynamic_dia>
	o<#self_id01> else
		o<select> CALL [32] [#<_metric>] [0.015] [0.4]
		#<_stepover_min> = #32
	o<#self_id01> endif
	#<_spindle_dir>      =  #param_spindle_dir
	#<_cooling_mode>     =  #param_cooling
	#<_feed_normal>      =  #param_feed
	#<_rpm_normal>       =  #param_speed
	#<_feed_vertical>    =  [#<_feed_normal> / 2]
	#<_penetration_mode> =  1
	#<_depth_step>       =  #param_stp
	#<_tool_usage>       =  0
	#<_stepover_normal>  = [#param_so / 100]
	#<_tool_dynamic_dia> =  0

	o<#self_id_tlc> if [[#param_tlc EQ 3] AND [#param_dnum GT 0]]
		M61 Q#param_dnum
	o<#self_id_tlc> endif

	o<#self_id_act> if [#param_act AND [#param_dnum NE #5400]]
		M9
		T#param_dnum M6
	o<#self_id_act> endif

	o<#self_id_lc> if [[#param_tlc EQ 1] OR [#param_tlc EQ 2]]
		G43 H#param_dnum
	o<#self_id_lc> endif

	o<#self_id_01> if [[#<_spindle_dir> GT 0] AND #<_spindle_all_time>]
		o<set_feed_rate_and_speed> CALL [1]
	o<#self_id_01> endif

	o<surf_finish> CALL [#<wp_left>] [#<wp_right>] [#<wp_front>] [#<wp_rear>] [#param_dir] [#param_mode + #param_entry] [#31] [#31 + #param_d] [#param_tc / 100] [#param_lst] [#param_touch]

	o<#self_id02> if [#<exists#ID>]
		#<_spindle_dir>      = #<spindle_dir#ID>
		#<_cooling_mode>     = #<cooling_mode#ID>
		#<_feed_normal>      = #<feed_normal#ID>
		#<_rpm_normal>       = #<rpm_normal#ID>
		#<_feed_vertical>    = #<feed_vertical#ID>
		#<_penetration_mode> = #<penetration_mode#ID>
		#<_depth_step>       = #<depth_step#ID>
		#<_tool_usage>       = #<tool_usage#ID>
		#<_stepover_normal>  = #<stepover_normal#ID>
		#<_tool_dynamic_dia> = #<tool_dynamic_dia#ID>
	o<#self_id02> endif

o<#self_id_active> endif
(end #sub_name)
```
