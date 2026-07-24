# "Line To"

>"<b>Create a line to X, Y</b>&#10;Absolute or Relative with optional styled corner"

| | |
|---|---|
| Type | `poly-line-to` |
| Icon | `line-to.png` |
| Source | `mill/polyline-to.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(line to absolute or relative position author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<select> CALL [31] [#param_ted] [#<poly_global_engagement>] [#param_te]

	o<poly_add_item> CALL [#param_type] [#param_x] [#param_y] [1] [#param_cs] [#param_cr] [#param_rev] [#31]

o<#self_id_active> endif
(end #sub_name)`

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
| | **"Milling"** | | |
| 11 | "Tool engagement" | Dropdown (editable) | `0` |
| 12 | "Tool engagement" | Integer | `100` |

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
- **Options**: "Relative=0:Absolute=1:X relative, Y absolute=10:X absolute, Y relative=11"

### "X"
- **NGC variable**: `#param_x`
- "Destination X"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y"
- **NGC variable**: `#param_y`
- "Destination Y"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Tool engagement"
- **NGC variable**: `#param_ted`
- "Tool engagement for this segment"
- **Options**: "Global=0:Specific=1"

### "Tool engagement"
- **NGC variable**: `#param_te`
- "Tool engagement"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(line to absolute or relative position author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<select> CALL [31] [#param_ted] [#<poly_global_engagement>] [#param_te]

	o<poly_add_item> CALL [#param_type] [#param_x] [#param_y] [1] [#param_cs] [#param_cr] [#param_rev] [#31]

o<#self_id_active> endif
(end #sub_name)
```
