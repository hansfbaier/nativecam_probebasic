# "End Mill Change"

>"<b>Change end mill and/or settings</b>&#10;Changes setting accordingly even if disabled"

| | |
|---|---|
| Type | `emill_chng` |
| Icon | `tool-01.png` |
| Source | `mill/sel-end-mill.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(end mill change params and changing code author : Fernand Veilleux)

#<_spindle_dir>      =  #param_spindle_dir
#<_cooling_mode>     =  #param_cooling

#<_feed_normal>      =  #param_feed
#<_rpm_normal>       =  #param_speed
#<_feed_vertical>    =  #param_v_feed
#<_penetration_mode> =  #param_pen
#<_depth_step>       =  #param_stp
#<_ramp_down_ratio>  = [#param_pr / 100]
#<_tool_usage>       =  #param_us
#<_stepover_min>     =  #param_so_m
#<_stepover_normal>  = [#param_so_n / 100]
#<_tool_dynamic_dia> =  #param_dd

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
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Select end mill"** | | |
| 3 | "Tool number" | tool | `0` |
| 4 | "Usage" | Dropdown | `0` |
| 5 | "Dynamic diameter" | Float | `0.0000` |
| | **"Action"** | | |
| 7 | "Use length comp" | Dropdown | `3` |
| 8 | "Start spindle" | Dropdown | `3` |
| 9 | "Use cooling" | Dropdown | `8` |
| | **"Feed and speed"** | | |
| 11 | "Feed" | Float | `10.0000` |
| 12 | "Vertical" | Float | `8.0000` |
| 13 | "Spindle speed" | Integer | `1000` |
| | **"Milling step over"** | | |
| 15 | "Expanding engagement" | Integer | `60` |
| 16 | "Minimum" | Float | `0.015` |
| | **"Penetration"** | | |
| 18 | "Mode" | Dropdown | `0` |
| 19 | "Step down" | Float | `-0.1250` |
| 20 | "Ramp down rate" | Integer | `25` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Params will be set even if disabled"

### "Tool number"
- **NGC variable**: `#param_dnum`
- "Select from tool table"

### "Usage"
- **NGC variable**: `#param_us`
- "Select usage for this tool"
- **Options**: "Roughing and finishing=0:Roughing=1:Finishing=2"

### "Dynamic diameter"
- **NGC variable**: `#param_dd`
- "Only for dynamic compensation, 0.0 to use diameter from table"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

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

### "Vertical"
- **NGC variable**: `#param_v_feed`
- "Plunge or drill feed"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Spindle speed"
- **NGC variable**: `#param_speed`
- "Set spindle speed"

### "Expanding engagement"
- **NGC variable**: `#param_so_n`
- "Maximum for pocketing or surface finishing"

### "Minimum"
- **NGC variable**: `#param_so_m`
- "Minimum"
- **Min**: 0.010  **Max**: 999999.9  **Digits**: 3

### "Mode"
- **NGC variable**: `#param_pen`
- "How Z position is attained"
- **Options**: "Ramp down=0:Plunge=1"

### "Step down"
- **NGC variable**: `#param_stp`
- "Step down on each pass"
- **Min**: -999999.9  **Max**: 0.0  **Digits**: 4

### "Ramp down rate"
- **NGC variable**: `#param_pr`
- "Z versus XY move"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(end mill change params and changing code author : Fernand Veilleux)

#<_spindle_dir>      =  #param_spindle_dir
#<_cooling_mode>     =  #param_cooling

#<_feed_normal>      =  #param_feed
#<_rpm_normal>       =  #param_speed
#<_feed_vertical>    =  #param_v_feed
#<_penetration_mode> =  #param_pen
#<_depth_step>       =  #param_stp
#<_ramp_down_ratio>  = [#param_pr / 100]
#<_tool_usage>       =  #param_us
#<_stepover_min>     =  #param_so_m
#<_stepover_normal>  = [#param_so_n / 100]
#<_tool_dynamic_dia> =  #param_dd

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
(end #sub_name)
```
