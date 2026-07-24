# "Mirror Polyline"

>"<b>Duplicate and reverse a polyline</b>"

| | |
|---|---|
| Type | `poly_miror_poly` |
| Icon | `polyline-mirrored.png` |
| Source | `mill/polyline-mirror-p.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(create a mirrored polyline from the previous one author : Fernand Veilleux)

o<#self_id_active> if  [#param_act AND [#<in_polyline> EQ 0] AND [#5000 GT 0]]

	o<poly_mirror_p> CALL [#param_ax]

	o<#self_id_rev> if [#param_dir]
		o<poly_reverse> CALL
	o<#self_id_rev> endif

	o<poly_copy_mill> CALL

	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<poly_mill> CALL [#<_mill_data_start>] [#31] [#32] [#param_comp] [#param_fcut] [#param_dx] [#param_dy] [#param_rot] [#param_gte / 100]

o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Offsets, rotation"** | | |
| 4 | "dX" | Float | `0.0000` |
| 5 | "dY" | Float | `0.0000` |
| 6 | "Rotation" | Float | `0.00` |
| | **"Mirror axis"** | | |
| 8 | "Axis" | Dropdown | `1` |
| | **"Milling"** | | |
| 10 | "Global tool engagement" | Float | `100` |
| 11 | "Tool compensation" | Dropdown | `40` |
| 12 | "Direction" | Dropdown | `0` |
| 13 | "Cut start" | Dropdown (editable) | `1` |
| 14 | "User start" | Float | `0.0000` |
| 15 | User gcode | G-code | `` |
| 16 | "Cut down to" | Dropdown (editable) | `1` |
| 17 | "User depth" | Float | `-0.5000` |
| 18 | User depth gcode | G-code | `` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_fcut`
- "Show design"

### "dX"
- **NGC variable**: `#param_dx`
- "Offset X"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "dY"
- **NGC variable**: `#param_dy`
- "Offset Y"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Rotation"
- **NGC variable**: `#param_rot`
- "Rotation center is origin"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Axis"
- **NGC variable**: `#param_ax`
- "Line or mirroring"
- **Options**: "X=1:Y=0"

### "Global tool engagement"
- **NGC variable**: `#param_gte`
- "Global tool engagement"
- **Min**: 0  **Max**: 100  **Digits**: 0

### "Tool compensation"
- **NGC variable**: `#param_comp`
- "Which side cutter will travel"
- **Options**: "None=40:Left=41:Right=42"

### "Direction"
- **NGC variable**: `#param_dir`
- "Mill as designed or in reverse"
- **Options**: "Designed=0:Reverse=1"

### "Cut start"
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
- **Options**: "User defined=0:Through=1:Bottom=2:Half=3:One quarter=4:Three quarter=5:G-Code=6"

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
(create a mirrored polyline from the previous one author : Fernand Veilleux)

o<#self_id_active> if  [#param_act AND [#<in_polyline> EQ 0] AND [#5000 GT 0]]

	o<poly_mirror_p> CALL [#param_ax]

	o<#self_id_rev> if [#param_dir]
		o<poly_reverse> CALL
	o<#self_id_rev> endif

	o<poly_copy_mill> CALL

	o<select> CALL [31] [#param_s] [#param_u_s] [#<surface>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugc]
	o<select> CALL [32] [#param_dpt] [#param_u_dpt] [#<bottom_through>] [#<bottom>] [#<surface> - #<wp_depth> / 2] [#<surface> - #<wp_depth> / 4] [#<bottom> + #<wp_depth> / 4] [#param_ugcd]

	o<poly_mill> CALL [#<_mill_data_start>] [#31] [#32] [#param_comp] [#param_fcut] [#param_dx] [#param_dy] [#param_rot] [#param_gte / 100]

o<#self_id_active> endif
(end #sub_name)
```
