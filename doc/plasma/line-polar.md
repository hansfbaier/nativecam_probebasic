# "Line Polar"

>"<b>Trace a line to a polar position</b>&#10;Relative with optional styled corner"

| | |
|---|---|
| Type | `poly_line_polar` |
| Icon | `line-polar.png` |
| Source | `plasma/polyline-polar.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(line to relative polar position author : Fernand Veilleux)
o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<poly_add_item> CALL [#param_type] [#param_l * COS[#param_a]] [#param_l * SIN[#param_a]] [1] [#param_cs] [#param_cr] [#param_rev] [100]
o<#self_id_active> endif`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Link"** | | |
| 3 | "Type" | Dropdown | `0` |
| 4 | "Radius" | Float | `0.3000` |
| 5 | "Complement" | Toggle | `0` |
| | **"Definition"** | | |
| 7 | "Angle" | Float | `60.00` |
| 8 | "Angle option" | Dropdown | `2` |
| 9 | "Length" | Float | `2.0000` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Type"
- **NGC variable**: `#param_cs`
- "Corner style to apply with previous item"
- **Options**: "None=0:Rounded=1:Beveled=2:Inverted Round=3"

### "Radius"
- **NGC variable**: `#param_cr`
- "Radius for rounded or distance from apex"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Complement"
- **NGC variable**: `#param_rev`
- "Reverse direction of tool path for rounded or inverted round"

### "Angle"
- **NGC variable**: `#param_a`
- "Angle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Angle option"
- **NGC variable**: `#param_type`
- "Angle relative to previous line or absolute"
- **Options**: "Absolute=2:Relative to previous line or chord=3:Relative to previous arc center=30"

### "Length"
- **NGC variable**: `#param_l`
- "Length of line"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(line to relative polar position author : Fernand Veilleux)
o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<poly_add_item> CALL [#param_type] [#param_l * COS[#param_a]] [#param_l * SIN[#param_a]] [1] [#param_cs] [#param_cr] [#param_rev] [100]
o<#self_id_active> endif
```
