# "Arc Polar Ctr"

>"<b>Add an arc to a polyline</b>&#10;Define center at polar position, angle where it ends and direction"

| | |
|---|---|
| Type | `poly_arc_polar_ctr` |
| Icon | `arc-polar-ctr.png` |
| Source | `mill/polyline-arc-polar.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(arc with center at a polar position author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<select> CALL [31] [#param_ted] [#<poly_global_engagement>] [#param_te]

	o<poly_add_item> CALL [#param_atype] [#param_cd] [#param_ca] [#param_dir] [#param_cs] [#param_cr] [#param_rev] [#31] [#param_a] [#param_etype]

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
| | **"Arc center"** | | |
| 7 | "Angle" | Float | `0.00` |
| 8 | "Angle option" | Dropdown | `8` |
| 9 | "Distance" | Float | `1.0000` |
| | **"Ending"** | | |
| 11 | "Angle" | Float | `180.00` |
| 12 | "Angle option" | Dropdown | `0` |
| 13 | "Direction" | Dropdown | `3` |
| | **"Milling"** | | |
| 15 | "Tool engagement" | Dropdown (editable) | `0` |
| 16 | "Tool engagement" | Integer | `100` |

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

### "Angle"
- **NGC variable**: `#param_ca`
- "Angle from start point"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Angle option"
- **NGC variable**: `#param_atype`
- "Angle relative to previous line or absolute"
- **Options**: "Absolute=8:Relative to previous line or chord=9:Relative to previous arc center=10"

### "Distance"
- **NGC variable**: `#param_cd`
- "Distance defines radius of arc"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

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
(arc with center at a polar position author : Fernand Veilleux)

o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<select> CALL [31] [#param_ted] [#<poly_global_engagement>] [#param_te]

	o<poly_add_item> CALL [#param_atype] [#param_cd] [#param_ca] [#param_dir] [#param_cs] [#param_cr] [#param_rev] [#31] [#param_a] [#param_etype]

o<#self_id_active> endif
(end #sub_name)
```
