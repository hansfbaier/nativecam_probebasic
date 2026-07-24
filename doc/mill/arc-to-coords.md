# "Arc To Coords"

>"<b>Add an arc to a polyline</b>&#10;Define destination, dir and arc height or radius"

| | |
|---|---|
| Type | `poly_arc_to_coords` |
| Icon | `arc-to-coords.png` |
| Source | `mill/polyline-arc-to.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(arc to absolute or relative coords author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<select> CALL [31] [#param_ted] [#<poly_global_engagement>] [#param_te]

	o<poly_add_item> CALL [#param_type] [#param_x] [#param_y] [#param_dir] [#param_cs] [#param_cr] [#param_rev0] [#31] [#param_height] [#param_atype] [#param_rev]

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
| | **"Arc end coords"** | | |
| 7 | "Option" | Dropdown | `4` |
| 8 | "X" | Float | `1.0000` |
| 9 | "Y" | Float | `1.0000` |
| | **"Definition"** | | |
| 11 | "Option" | Dropdown | `0` |
| 12 | "Size" | Float | `1.0000` |
| 13 | "Flip center" | Toggle | `0` |
| 14 | "Direction" | Dropdown | `2` |
| | **"Milling"** | | |
| 16 | "Tool engagement" | Dropdown (editable) | `0` |
| 17 | "Tool engagement" | Integer | `100` |

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
- **NGC variable**: `#param_rev0`
- "Reverse direction of tool path for rounded or inverted round"

### "Option"
- **NGC variable**: `#param_type`
- "Select Relative or Absolute"
- **Options**: "Relative=4:Absolute=5:X relative, Y absolute=41:X absolute, Y relative=42"

### "X"
- **NGC variable**: `#param_x`
- "Destination X"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y"
- **NGC variable**: `#param_y`
- "Destination Y"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Option"
- **NGC variable**: `#param_atype`
- "Select value defined"
- **Options**: "Radius=0:Arc height=1"

### "Size"
- **NGC variable**: `#param_height`
- "Size"
- **Min**: 0  **Max**: 999999.9  **Digits**: 4

### "Flip center"
- **NGC variable**: `#param_rev`
- "Center opposite side of chord"

### "Direction"
- **NGC variable**: `#param_dir`
- "Direction of path"
- **Options**: "Clockwise=2:Counter-Clockwise=3"

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
(arc to absolute or relative coords author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<select> CALL [31] [#param_ted] [#<poly_global_engagement>] [#param_te]

	o<poly_add_item> CALL [#param_type] [#param_x] [#param_y] [#param_dir] [#param_cs] [#param_cr] [#param_rev0] [#31] [#param_height] [#param_atype] [#param_rev]

o<#self_id_active> endif
(end #sub_name)
```
