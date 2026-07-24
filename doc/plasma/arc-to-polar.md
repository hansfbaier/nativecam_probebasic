# "Arc To Polar"

>"<b>Add an arc to a polyline</b>&#10;Define polar destination, dir and arc height or radius"

| | |
|---|---|
| Type | `poly_arc_to_polar` |
| Icon | `arc-polar.png` |
| Source | `plasma/polyline-arc-top.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(arc to polar destination author : Fernand Veilleux)
o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<poly_add_item> CALL [4] [#param_cl * COS[#param_ca]] [#param_cl * SIN[#param_ca]] [#param_dir] [#param_cs] [#param_cr] [#param_rev0] [100] [#param_height] [#param_atype] [#param_rev]
o<#self_id_active> endif`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Link"** | | |
| 3 | "Type" | Dropdown | `0` |
| 4 | "Radius" | Float | `0.3000` |
| 5 | "Complement" | Toggle | `0` |
| | **"Arc end"** | | |
| 7 | "Chord length" | Float | `1.0000` |
| 8 | "Angle" | Float | `0.00` |
| | **"Definition"** | | |
| 10 | "Option" | Dropdown | `0` |
| 11 | "Size" | Float | `1.0000` |
| 12 | "Flip center" | Toggle | `0` |
| 13 | "Direction" | Dropdown | `2` |

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

### "Chord length"
- **NGC variable**: `#param_cl`
- "Center of arc will be calculated"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Angle"
- **NGC variable**: `#param_ca`
- "Angle from start point"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

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

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(arc to polar destination author : Fernand Veilleux)
o<#self_id_active> if [#param_act AND #<in_polyline>]
	o<poly_add_item> CALL [4] [#param_cl * COS[#param_ca]] [#param_cl * SIN[#param_ca]] [#param_dir] [#param_cs] [#param_cr] [#param_rev0] [100] [#param_height] [#param_atype] [#param_rev]
o<#self_id_active> endif
```
