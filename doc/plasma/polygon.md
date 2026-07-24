# "Polygon"

>"<b>Create a Polygon with n edges</b>"

| | |
|---|---|
| Type | `polygon` |
| Icon | `hexagon.png` |
| Source | `plasma/polygon.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(polygon of #param_n edges author : Fernand Veilleux)
o<#self_id_active> if [#param_act] (if active)
	o<polygon> CALL [#param_cx] [#param_cy] [#param_n] [#param_r] [#param_rot] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_pv]
o<#self_id_active> endif`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords"** | | |
| 4 | "cX" | Float | `0.0000` |
| 5 | "cY" | Float | `0.0000` |
| | **"Size, rotation"** | | |
| 7 | "Edges count" | Integer | `6` |
| 8 | "Radius" | Float | `1.0000` |
| 9 | "Rotation" | Float | `0.00` |
| | **"Cutting"** | | |
| 11 | "Option" | Dropdown | `0` |
| 12 | "Direction" | Dropdown | `3` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_pv`
- "Show design"

### "cX"
- **NGC variable**: `#param_cx`
- "Polygon center X"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "cY"
- **NGC variable**: `#param_cy`
- "Polygon center Y"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Edges count"
- **NGC variable**: `#param_n`
- "Number of edges"

### "Radius"
- **NGC variable**: `#param_r`
- "Radius"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Rotation"
- **NGC variable**: `#param_rot`
- "Start angle"
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
(polygon of #param_n edges author : Fernand Veilleux)
o<#self_id_active> if [#param_act] (if active)
	o<polygon> CALL [#param_cx] [#param_cy] [#param_n] [#param_r] [#param_rot] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_pv]
o<#self_id_active> endif
```
