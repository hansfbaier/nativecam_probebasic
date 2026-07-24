# "Mirror Polyline"

>"<b>Duplicate and reverse a polyline</b>"

| | |
|---|---|
| Type | `poly_mirror_poly` |
| Icon | `polyline-mirrored.png` |
| Source | `plasma/polyline-mirror-p.cfg` |

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

	o<poly_mill> CALL [#<_mill_data_start>] [#<pl_cut_start>] [#<pl_cut_start>] [#param_comp] [#param_fcut] [#param_dx] [#param_dy] [#param_rot]

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
| | **"Cutting"** | | |
| 10 | "Cut width compensation" | Dropdown | `40` |
| 11 | "Direction" | Dropdown | `0` |

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

### "Cut width compensation"
- **NGC variable**: `#param_comp`
- "Which side cutter will travel"
- **Options**: "None=40:Left=41:Right=42"

### "Direction"
- **NGC variable**: `#param_dir`
- "Cut as designed or in reverse"
- **Options**: "Designed=0:Reverse=1"

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

	o<poly_mill> CALL [#<_mill_data_start>] [#<pl_cut_start>] [#<pl_cut_start>] [#param_comp] [#param_fcut] [#param_dx] [#param_dy] [#param_rot]

o<#self_id_active> endif
(end #sub_name)
```
