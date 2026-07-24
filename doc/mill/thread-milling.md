# "Thread Milling"

>"<b>Create internal or external threads</b>"

| | |
|---|---|
| Type | `thread-milling` |
| Icon | `threading-v.png` |
| Source | `mill/thread-milling.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(authors : Fernand Veilleux and Philip Mullen)

o<#self_id_active> if [#param_act AND [#<_tool_usage> EQ 4]] (if active)
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<thread-milling> CALL [#param_cx] [#param_al_x] [#param_cy] [#param_al_y] [#param_maj_d] [#param_min_d] [#param_pitch] [#param_m_i] [#param_starts] [#param_rot] [#param_opt] [#param_dir] [#31] [#32] [#param_pv] [0]

o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords, size"** | | |
| 4 | "cX" | Float | `0.0000` |
| 5 | "X axis align" | Dropdown | `1` |
| 6 | "cY" | Float | `0.0000` |
| 7 | "Y axis align" | Dropdown | `1` |
| | **"Milling"** | | |
| 9 | "Option" | Dropdown | `2` |
| 10 | "Direction" | Dropdown | `3` |
| 11 | "Rotation" | Float | `0.00` |
| 12 | "Helix top" | Dropdown (editable) | `1` |
| 13 | "User top" | Float | `0.0000` |
| 14 | User gcode | G-code | `` |
| 15 | "Helix bottom" | Dropdown (editable) | `1` |
| 16 | "User bottom" | Float | `-0.5000` |
| 17 | User depth gcode | G-code | `` |
| | **"Helix"** | | |
| 19 | "Units" | Dropdown | `0` |
| 20 | "Major diameter" | Float | `1.0000` |
| 21 | "Minor diameter" | Float | `0.8000` |
| 22 | "Pitch" | Float | `12.0000` |
| 23 | "Starts" | Integer | `1` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_pv`
- "Show design"

### "cX"
- **NGC variable**: `#param_cx`
- "Center of helix"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X axis align"
- **NGC variable**: `#param_al_x`
- "Define X reference point"
- **Options**: "Left=0:Center=1:Right=2"

### "cY"
- **NGC variable**: `#param_cy`
- "Center of helix"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y axis align"
- **NGC variable**: `#param_al_y`
- "Define Y reference point"
- **Options**: "Top=0:Center=1:Bottom=2"

### "Option"
- **NGC variable**: `#param_opt`
- "Select helix side"
- **Options**: "Internal=2:External=3"

### "Direction"
- **NGC variable**: `#param_dir`
- "Direction of path"
- **Options**: "Clockwise (RH)=3:Counter-clockwise (LH)=2"

### "Rotation"
- **NGC variable**: `#param_rot`
- "Rotation of start location"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Helix top"
- **NGC variable**: `#param_s`
- "Pre or user defined"
- **Options**: "User defined=0:Surface=1:Half=2:One quarter=3:Three quarter=4:G-Code=5"

### "User top"
- **NGC variable**: `#param_u_s`
- "User top"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### User gcode
- **NGC variable**: `#param_ugc`
- User gcode

### "Helix bottom"
- **NGC variable**: `#param_dpt`
- "Pre or user defined"
- **Options**: "User defined=0:Through=1:Bottom=2:Half=3:One quarter=4:Three quarter=5:G-Code=6"

### "User bottom"
- **NGC variable**: `#param_u_dpt`
- "User bottom"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### User depth gcode
- **NGC variable**: `#param_ugcd`
- User depth gcode

### "Units"
- **NGC variable**: `#param_m_i`
- "Units"
- **Options**: "Imperial=0:Metric=1"

### "Major diameter"
- **NGC variable**: `#param_maj_d`
- "Major diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Minor diameter"
- **NGC variable**: `#param_min_d`
- "Minor diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Pitch"
- **NGC variable**: `#param_pitch`
- "Metric pitch is thread to thread, imperial is per inch"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Starts"
- **NGC variable**: `#param_starts`
- "Number of helix"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(authors : Fernand Veilleux and Philip Mullen)

o<#self_id_active> if [#param_act AND [#<_tool_usage> EQ 4]] (if active)
	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<thread-milling> CALL [#param_cx] [#param_al_x] [#param_cy] [#param_al_y] [#param_maj_d] [#param_min_d] [#param_pitch] [#param_m_i] [#param_starts] [#param_rot] [#param_opt] [#param_dir] [#31] [#32] [#param_pv] [0]

o<#self_id_active> endif
(end #sub_name)
```
