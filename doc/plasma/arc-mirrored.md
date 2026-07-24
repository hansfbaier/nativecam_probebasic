# "Arc Mirrored"

>"<b>Add an mirrored arc to a polyline</b>&#10;Define mirror line, I and J offsets, angle and direction"

| | |
|---|---|
| Type | `poly_arc_bisector` |
| Icon | `polyline-mirrored.png` |
| Source | `plasma/polyline-arc-m.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(arc mirrored with I,J offsets or absolute center author : Fernand Veilleux)
o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<poly_add_item> CALL [#param_type] [#param_i] [#param_j] [#param_dir] [#param_cs] [#param_cr] [#param_rev] [100] [#param_x] [#param_y] [#param_sl]
o<#self_id_active> endif`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Link"** | | |
| 3 | "Type" | Dropdown | `0` |
| 4 | "Radius" | Float | `0.3000` |
| 5 | "Complement" | Toggle | `0` |
| | **"Arc center"** | | |
| 7 | "Using" | Dropdown | `14` |
| 8 | "I offset or cX" | Float | `1.0000` |
| 9 | "J offset or cY" | Float | `0.0000` |
| | **"Mirror line end"** | | |
| 11 | "X" | Float | `3.0000` |
| 12 | "Y" | Float | `0.0000` |
| 13 | "Show line" | Toggle | `1` |
| 14 | "Direction" | Dropdown | `3` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Type"
- **NGC variable**: `#param_cs`
- "Select link type"
- **Options**: "None=0:Rounded=1:Beveled=2:Inverted Round=3"

### "Radius"
- **NGC variable**: `#param_cr`
- "Radius for rounded or distance from apex"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Complement"
- **NGC variable**: `#param_rev`
- "Reverse direction of tool path for rounded or inverted round"

### "Using"
- **NGC variable**: `#param_type`
- "Arc center option"
- **Options**: "Offsets=14:Absolute position=15"

### "I offset or cX"
- **NGC variable**: `#param_i`
- "Offset or absolute value"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "J offset or cY"
- **NGC variable**: `#param_j`
- "Offset or absolute value"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X"
- **NGC variable**: `#param_x`
- "Mirror line end"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y"
- **NGC variable**: `#param_y`
- "Mirror line end"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Show line"
- **NGC variable**: `#param_sl`
- "Show line"

### "Direction"
- **NGC variable**: `#param_dir`
- "Direction of path"
- **Options**: "Clockwise=2:Counter-Clockwise=3"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(arc mirrored with I,J offsets or absolute center author : Fernand Veilleux)
o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<poly_add_item> CALL [#param_type] [#param_i] [#param_j] [#param_dir] [#param_cs] [#param_cr] [#param_rev] [100] [#param_x] [#param_y] [#param_sl]
o<#self_id_active> endif
```
