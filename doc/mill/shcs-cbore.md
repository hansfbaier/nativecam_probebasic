# "SHCS CBore"

>"<b>Creates a counterbore for a socket head cap screw</b>&#10;Will mill the screw hole if tool is small enough&#10;<span foreground='blue' style='oblique'><b>Message possible in terminal window</b></span>"

| | |
|---|---|
| Type | `shcs_cbore` |
| Icon | `shcs-hole.png` |
| Source | `mill/SHCS.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(hole with counterbore author : Fernand Veilleux)

o<#self_id_active> if [#param_act]
	o<select> CALL [31] [#param_st] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_usd] [#<bottom_through>] [#<bottom>] [#param_ugcd]
	o<select> CALL [33] [#param_bore_d] [#param_u_depth] [0] [0] [#param_u_dgc]

	o<shcs_size> CALL [#param_screw] [#param_scr_f] [#param_scr_m] [#param_scr_n] [#param_wd] [#param_wt] [#param_bore_d] [#33] [#31] [#<bottom>]

	#<spindle_all_time#ID> = #<_spindle_all_time>
	#<_spindle_all_time>   = 1
	o<circle> CALL [#param_cx] [#param_cy] [#<_shcs_bore_dia>] [0] [0] [1] [#param_dir] [#31] [#<_shcs_bore_depth>] [#param_pv]
	#<_spindle_all_time>   = #<spindle_all_time#ID>

	o<#self_id_00> if [#<_shcs_body_dia> GE [#5410 * 0.9]]
		o<circle> CALL [#param_cx] [#param_cy] [#<_shcs_body_dia>] [0] [0] [0] [#param_dir] [#<_shcs_bore_depth>] [#32] [#param_pv]
	o<#self_id_00> else
		(print,)
		(print,Tool is too large to mill bolt diameter hole, use a drill at least #<_shcs_body_dia> in diameter)
		o<#self_id11> if [#<_spindle_all_time> EQ 0]
			M9 M5
		o<#self_id11> endif
	o<#self_id_00> endif

o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords"** | | |
| 4 | "cX" | Float | `0.0000` |
| 5 | "cY" | Float | `0.0000` |
| | **"Screw"** | | |
| 7 | "Select size" | Dropdown (editable) | `1` |
| 8 | "Fractional" | List | `32` |
| 9 | "Metric" | List | `7` |
| 10 | "Numbered screw" | List | `58` |
| 11 | "Counterbore depth" | Dropdown (editable) | `2` |
| 12 | User defined depth | Float | `-0.3000` |
| 13 | User defined depth | G-code | `` |
| | **"Washer"** | | |
| 15 | "Diameter" | Float | `0.0000` |
| 16 | "Thickness" | Float | `0.0000` |
| | **"Milling"** | | |
| 18 | "Direction" | Dropdown | `3` |
| 19 | "Cut start" | Dropdown (editable) | `1` |
| 20 | User start | Float | `0.0000` |
| 21 | "Cut down to" | Dropdown (editable) | `1` |
| 22 | User gcode | G-code | `` |
| 23 | User depth | Float | `0.0000` |
| 24 | User depth gcode | G-code | `` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_pv`
- "Show design"

### "cX"
- **NGC variable**: `#param_cx`
- "Center of hole"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "cY"
- **NGC variable**: `#param_cy`
- "Center of hole"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Select size"
- **NGC variable**: `#param_screw`
- "Select metric, fractional or numbered"
- **Options**: "Fractional=1:Metric=2:Number=3"

### "Fractional"
- **NGC variable**: `#param_scr_f`
- "Fractional"
- **Options**: 1/4=31:5/16=32:3/8=33:7/16=34:1/2=35:9/16=36:5/8=37:3/4=38:7/8=39:1=10:1 1/8=41:1 1/4=42:1 1/2=43:1 3/4=44:2=45

### "Metric"
- **NGC variable**: `#param_scr_m`
- "Metric"
- **Options**: 1.6=1:2=2:2.5=3:2.6=4:3=5:4=6:5=7:6=8:8=9:10=10:12=11:14=12:16=13:18=14:20=15:24=16:30=17:36=18:42=19:48=20

### "Numbered screw"
- **NGC variable**: `#param_scr_n`
- "Numbered screw"
- **Options**: 0=51:1=52:2=53:3=54:4=55:5=56:6=57:8=58:10=59:12=60

### "Counterbore depth"
- **NGC variable**: `#param_bore_d`
- "Or head under surface or&#10;leave material equal to screw diameter"
- **Options**: "User defined=0:Head clears surface=1:Maximum depth=2:G-Code=3"

### User defined depth
- **NGC variable**: `#param_u_depth`
- User defined depth
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### User defined depth
- **NGC variable**: `#param_u_dgc`
- User defined depth

### "Diameter"
- **NGC variable**: `#param_wd`
- "Diameter of washer used if any in usual units (specify a little larger to clear)"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Thickness"
- **NGC variable**: `#param_wt`
- "Thickness of washer used if any in usual units"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Direction"
- **NGC variable**: `#param_dir`
- "Direction of path"
- **Options**: "Clockwise=2:Counter-Clockwise=3"

### "Cut start"
- **NGC variable**: `#param_st`
- "Pre or user defined"
- **Options**: "User defined=0:Surface=1:Half=2:One quarter=3:Three quarter=4:G-Code=5"

### User start
- **NGC variable**: `#param_u_s`
- User start
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Cut down to"
- **NGC variable**: `#param_dpt`
- "Pre defined"
- **Options**: "User defined=0:Through=1:Bottom=2:G-Code=3"

### User gcode
- **NGC variable**: `#param_ugc`
- User gcode

### User depth
- **NGC variable**: `#param_usd`
- User depth
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### User depth gcode
- **NGC variable**: `#param_ugcd`
- User depth gcode

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(hole with counterbore author : Fernand Veilleux)

o<#self_id_active> if [#param_act]
	o<select> CALL [31] [#param_st] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_usd] [#<bottom_through>] [#<bottom>] [#param_ugcd]
	o<select> CALL [33] [#param_bore_d] [#param_u_depth] [0] [0] [#param_u_dgc]

	o<shcs_size> CALL [#param_screw] [#param_scr_f] [#param_scr_m] [#param_scr_n] [#param_wd] [#param_wt] [#param_bore_d] [#33] [#31] [#<bottom>]

	#<spindle_all_time#ID> = #<_spindle_all_time>
	#<_spindle_all_time>   = 1
	o<circle> CALL [#param_cx] [#param_cy] [#<_shcs_bore_dia>] [0] [0] [1] [#param_dir] [#31] [#<_shcs_bore_depth>] [#param_pv]
	#<_spindle_all_time>   = #<spindle_all_time#ID>

	o<#self_id_00> if [#<_shcs_body_dia> GE [#5410 * 0.9]]
		o<circle> CALL [#param_cx] [#param_cy] [#<_shcs_body_dia>] [0] [0] [0] [#param_dir] [#<_shcs_bore_depth>] [#32] [#param_pv]
	o<#self_id_00> else
		(print,)
		(print,Tool is too large to mill bolt diameter hole, use a drill at least #<_shcs_body_dia> in diameter)
		o<#self_id11> if [#<_spindle_all_time> EQ 0]
			M9 M5
		o<#self_id11> endif
	o<#self_id_00> endif

o<#self_id_active> endif
(end #sub_name)
```
