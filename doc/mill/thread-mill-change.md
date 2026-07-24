# "Thread Mill Change"

>"<b>Change thread mill and/or settings</b>&#10;Changes setting accordingly even if disabled"

| | |
|---|---|
| Type | `tmill_chng` |
| Icon | `tool-change.png` |
| Source | `mill/sel-thread-mill.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(thread mill change params and changing code author : Fernand Veilleux)

#<_spindle_dir>      =  #param_spindle_dir
#<_cooling_mode>     =  #param_cooling

#<_feed_normal>      =  #param_feed
#<_rpm_normal>       =  #param_speed
#<_feed_vertical>    =  #param_v_feed
#<_tool_usage>       =  4
#<_thread_cut_depth> =  #param_cut_depth
#<_thread_cut_teeth> =  #param_cut_teeth
#<_thread_lead_in>   =  #param_lead_clearance

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
| | **"Select thread mill"** | | |
| 3 | "Tool number" | tool | `0` |
| | **"Action"** | | |
| 5 | "Use length comp" | Dropdown | `3` |
| 6 | "Start spindle" | Dropdown | `3` |
| 7 | "Use cooling" | Dropdown | `8` |
| | **"Feed and speed"** | | |
| 9 | "Feed" | Float | `10.0000` |
| 10 | "Vertical" | Float | `8.0000` |
| 11 | "Spindle speed" | Integer | `1000` |
| | **"Params"** | | |
| 13 | "Lead-in clearance" | Float | `0.0400` |
| 14 | "Cutter engagement" | Float | `0.0200` |
| 15 | "Cutter teeth" | Integer | `1` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Params will be set even if disabled"

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

### "Vertical"
- **NGC variable**: `#param_v_feed`
- "Plunge or drill feed"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Spindle speed"
- **NGC variable**: `#param_speed`
- "Set spindle speed"

### "Lead-in clearance"
- **NGC variable**: `#param_lead_clearance`
- "Distance from face in machine units before engaging cutter"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Cutter engagement"
- **NGC variable**: `#param_cut_depth`
- "Depth of cutter engagment in machine units per pass"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Cutter teeth"
- **NGC variable**: `#param_cut_teeth`
- "Number of cutter teeth"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(thread mill change params and changing code author : Fernand Veilleux)

#<_spindle_dir>      =  #param_spindle_dir
#<_cooling_mode>     =  #param_cooling

#<_feed_normal>      =  #param_feed
#<_rpm_normal>       =  #param_speed
#<_feed_vertical>    =  #param_v_feed
#<_tool_usage>       =  4
#<_thread_cut_depth> =  #param_cut_depth
#<_thread_cut_teeth> =  #param_cut_teeth
#<_thread_lead_in>   =  #param_lead_clearance

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
