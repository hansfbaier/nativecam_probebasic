# "Line To"

>"<b>Create a line to X, Y</b>&#10;Absolute or Relative with optional styled corner"

| | |
|---|---|
| Type | `poly_line_to` |
| Icon | `line-to.png` |
| Source | `plasma/polyline-to.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(line to absolute or relative position author : Fernand Veilleux)
o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<poly_add_item> CALL [#param_type] [#param_x] [#param_y] [1] [#param_cs] [#param_cr] [#param_rev] [100]
o<#self_id_active> endif`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Link"** | | |
| 3 | "Type" | Dropdown | `0` |
| 4 | "Radius" | Float | `0.3000` |
| 5 | "Complement" | Toggle | `0` |
| | **"Coords"** | | |
| 7 | "Option" | Dropdown | `0` |
| 8 | "X" | Float | `1.0000` |
| 9 | "Y" | Float | `1.0000` |

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

### "Option"
- **NGC variable**: `#param_type`
- "Select Relative or Absolute"
- **Options**: "Relative=0:Absolute=1"

### "X"
- **NGC variable**: `#param_x`
- "Destination X"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y"
- **NGC variable**: `#param_y`
- "Destination Y"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(line to absolute or relative position author : Fernand Veilleux)
o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<poly_add_item> CALL [#param_type] [#param_x] [#param_y] [1] [#param_cs] [#param_cr] [#param_rev] [100]
o<#self_id_active> endif
```
