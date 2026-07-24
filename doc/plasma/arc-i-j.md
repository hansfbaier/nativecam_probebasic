# "Arc I,J"

>"<b>Add an arc to a polyline</b>&#10;Define I and J offsets, angle and direction"

| | |
|---|---|
| Type | `poly_arc_IJ` |
| Icon | `arc-to-ij.png` |
| Source | `plasma/polyline-arc-ij.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(arc with I,J offsets or absolute center author : Fernand Veilleux)
o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<poly_add_item> CALL [#param_type] [#param_i] [#param_j] [#param_dir] [#param_cs] [#param_cr] [#param_rev] [100] [#param_a] [#param_etype]
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
| 7 | "Using" | Dropdown | `6` |
| 8 | "I offset or cX" | Float | `1.0000` |
| 9 | "J offset or cY" | Float | `0.0000` |
| | **"Ending"** | | |
| 11 | "Angle" | Float | `60.00` |
| 12 | "Angle option" | Dropdown | `0` |
| 13 | "Direction" | Dropdown | `3` |

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
- **Options**: "Offsets=6:Absolute position=7"

### "I offset or cX"
- **NGC variable**: `#param_i`
- "Offset or absolute value"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "J offset or cY"
- **NGC variable**: `#param_j`
- "Offset or absolute value"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Angle"
- **NGC variable**: `#param_a`
- "Angle where it ends"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Angle option"
- **NGC variable**: `#param_etype`
- "Angle relative to beginning of arc or absolute"
- **Options**: "Relative to start=0:Absolute to arc center=1"

### "Direction"
- **NGC variable**: `#param_dir`
- "Direction of path"
- **Options**: "Clockwise=2:Counter-Clockwise=3"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(arc with I,J offsets or absolute center author : Fernand Veilleux)
o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<poly_add_item> CALL [#param_type] [#param_i] [#param_j] [#param_dir] [#param_cs] [#param_cr] [#param_rev] [100] [#param_a] [#param_etype]
o<#self_id_active> endif
```
