# "Circle by Center"

>"<b>Create a Circle from it's center</b>&#10;Can add a flat"

| | |
|---|---|
| Type | `circle` |
| Icon | `circle.png` |
| Source | `plasma/circle.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(circle from center author : Fernand Veilleux)
o<#self_id_active> if [#param_act] (if active)
	o<select> CALL [33] [#param_al_x] [#param_d / 2] [0] [-#param_d / 2]
	o<select> CALL [34] [#param_al_y] [-#param_d / 2] [0] [#param_d / 2]

	o<circle> CALL [#param_cx + #33] [#param_cy + #34] [#param_d] [#param_f] [#param_rot] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_pv]
o<#self_id_active> endif`

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
| 8 | "Diameter" | Float | `1.5000` |
| | **"D flat"** | | |
| 10 | "Remove" | Float | `0.0000` |
| 11 | "Rotation" | Float | `0.00` |
| | **"Cutting"** | | |
| 13 | "Option" | Dropdown | `0` |
| 14 | "Direction" | Dropdown | `3` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_pv`
- "Show design"

### "cX"
- **NGC variable**: `#param_cx`
- "Center of circle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X axis align"
- **NGC variable**: `#param_al_x`
- "Define X reference point"
- **Options**: "Left=0:Center=1:Right=2"

### "cY"
- **NGC variable**: `#param_cy`
- "Center of circle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y axis align"
- **NGC variable**: `#param_al_y`
- "Define Y reference point"
- **Options**: "Top=0:Center=1:Bottom=2"

### "Diameter"
- **NGC variable**: `#param_d`
- "Diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Remove"
- **NGC variable**: `#param_f`
- "Height to remove from diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Rotation"
- **NGC variable**: `#param_rot`
- "Rotation of flat"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Option"
- **NGC variable**: `#param_opt`
- "Select tool path"
- **Options**: "Inside=0:On the line=2:Outside=3"

### "Direction"
- **NGC variable**: `#param_dir`
- "Direction of path"
- **Options**: "Clockwise=2:Counter-Clockwise=3"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(circle from center author : Fernand Veilleux)
o<#self_id_active> if [#param_act] (if active)
	o<select> CALL [33] [#param_al_x] [#param_d / 2] [0] [-#param_d / 2]
	o<select> CALL [34] [#param_al_y] [-#param_d / 2] [0] [#param_d / 2]

	o<circle> CALL [#param_cx + #33] [#param_cy + #34] [#param_d] [#param_f] [#param_rot] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_pv]
o<#self_id_active> endif
```
