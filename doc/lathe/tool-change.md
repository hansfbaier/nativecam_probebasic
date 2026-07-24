# "Tool Change"

>"<b>Change Tool and/or settings</b>&#10;Changes setting accordingly even if disabled"

| | |
|---|---|
| Type | `tool_change` |
| Icon | `lathe-tool-change.png` |
| Source | `lathe/tool-change.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_tlc> if [[#param_tlc EQ 3] AND [#param_dnum GT 0]]
	M61 Q#param_dnum
o<#self_id_tlc> endif

o<#self_id_act> if [#param_act AND [#param_dnum NE #5400]]
	M9  (coolant off)
	T#param_dnum M6
o<#self_id_act> endif

o<#self_id_lc> if [#param_tlc GE 1]
	G43 H#param_dnum
o<#self_id_lc> endif

#<_tool_usage>   =  #param_us
#<_spindle_dir>  =  #param_spindle_dir
#<_cooling_mode> =  #param_cooling

#<_rough_feed>   =  #param_r_feed
#<_rough_cut>    =  #param_c_dpt

#<_finish_feed>  =  #param_f_feed
#<_finish_cut>   =  #param_fc_dpt

o<#self_id1> if [#param_mode EQ 0]
	G96 D#param_speed S#param_surf_speed
o<#self_id1> else
	G97 S#param_speed
o<#self_id1> endif

o<#self_id2> if [#<_spindle_dir> GT 0]
	M#<_spindle_dir>
	G4 P#<_spindle_speed_up_delay>
o<#self_id2> endif

#<_z_clear>  = [#5410 + #param_rz]
#<_x_clear>  = [[#5410 + #param_rx] * #<_diameter_mode>]
#<_ix_clear> = [#param_rix * #<_diameter_mode>]

F#<_rough_feed>

(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Tool and usage"** | | |
| 3 | "Tool number" | tool | `0` |
| 4 | "Usage" | Dropdown | `0` |
| 5 | "Use length comp" | Dropdown | `1` |
| 6 | "Start spindle" | Dropdown | `3` |
| 7 | "Use cooling" | Dropdown | `8` |
| | **"Spindle control"** | | |
| 9 | "Mode" | Dropdown | `1` |
| 10 | "Max spindle" | Integer | `500` |
| 11 | "Surface speed" | Integer | `100` |
| | **"Roughing"** | | |
| 13 | "Feed" | Float | `3.0000` |
| 14 | "Cut depth" | Float | `0.0200` |
| | **"Finishing"** | | |
| 16 | "Feed" | Float | `2.0000` |
| 17 | "Cut depth" | Float | `0.0100` |
| | **"Clearances"** | | |
| 19 | "Retract X" | Float | `0.0400` |
| 20 | "Int. retract X" | Float | `0.0400` |
| 21 | "Retract Z" | Float | `0.0400` |

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

### "Use length comp"
- **NGC variable**: `#param_tlc`
- "Use G43 and probe if setup"
- **Options**: "No=0:Already mounted and touched=3:From tool table=1:Table and probe=2"

### "Start spindle"
- **NGC variable**: `#param_spindle_dir`
- "Select spindle rotation"
- **Options**: "No=5:Clockwise=3:Counter-clockwise=4"

### "Use cooling"
- **NGC variable**: `#param_cooling`
- "Use flood, mist or none"
- **Options**: "None=9:Flood=8:Mist=7"

### "Mode"
- **NGC variable**: `#param_mode`
- "Mode"
- **Options**: "Constant surface speed=0:RPM=1"

### "Max spindle"
- **NGC variable**: `#param_speed`
- "RPM spindle speed"

### "Surface speed"
- **NGC variable**: `#param_surf_speed`
- "Constant spindle speed"

### "Feed"
- **NGC variable**: `#param_r_feed`
- "Feed at 100% engagement"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Cut depth"
- **NGC variable**: `#param_c_dpt`
- "Depth of cutter engagment in machine units per pass"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Feed"
- **NGC variable**: `#param_f_feed`
- "Feed at 100% engagement"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Cut depth"
- **NGC variable**: `#param_fc_dpt`
- "Depth of cutter engagment in machine units per pass"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Retract X"
- **NGC variable**: `#param_rx`
- "Retract distance on multiple passes"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Int. retract X"
- **NGC variable**: `#param_rix`
- "Retract distance"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Retract Z"
- **NGC variable**: `#param_rz`
- "Retract distance on multiple passes"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_tlc> if [[#param_tlc EQ 3] AND [#param_dnum GT 0]]
	M61 Q#param_dnum
o<#self_id_tlc> endif

o<#self_id_act> if [#param_act AND [#param_dnum NE #5400]]
	M9  (coolant off)
	T#param_dnum M6
o<#self_id_act> endif

o<#self_id_lc> if [#param_tlc GE 1]
	G43 H#param_dnum
o<#self_id_lc> endif

#<_tool_usage>   =  #param_us
#<_spindle_dir>  =  #param_spindle_dir
#<_cooling_mode> =  #param_cooling

#<_rough_feed>   =  #param_r_feed
#<_rough_cut>    =  #param_c_dpt

#<_finish_feed>  =  #param_f_feed
#<_finish_cut>   =  #param_fc_dpt

o<#self_id1> if [#param_mode EQ 0]
	G96 D#param_speed S#param_surf_speed
o<#self_id1> else
	G97 S#param_speed
o<#self_id1> endif

o<#self_id2> if [#<_spindle_dir> GT 0]
	M#<_spindle_dir>
	G4 P#<_spindle_speed_up_delay>
o<#self_id2> endif

#<_z_clear>  = [#5410 + #param_rz]
#<_x_clear>  = [[#5410 + #param_rx] * #<_diameter_mode>]
#<_ix_clear> = [#param_rix * #<_diameter_mode>]

F#<_rough_feed>

(end #sub_name)
```
