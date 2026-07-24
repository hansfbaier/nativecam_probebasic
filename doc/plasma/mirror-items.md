# "Mirror Items"

>"<b>Duplicate and reverse polyline items</b>"

| | |
|---|---|
| Type | `poly_mirror_itms` |
| Icon | `polyline-mirror-items.png` |
| Source | `plasma/polyline-mirror-i.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(mirror polyline items author : Fernand Veilleux)
o<#self_id_active> if [#<in_polyline> AND #param_act AND [#5000 GE 1] AND [[#param_x1 NE #param_x2] OR [#param_y1 NE #param_y2]]]
/	o<#self_id0> if [#param_show]
/		o<#self_id1> if [#<_has_z_axis>]
/			G0 X#param_x1 Y#param_y1 Z#<surface>
/		o<#self_id1> else
/			G0 X#param_x1 Y#param_y1
/		o<#self_id1> endif
/		G1 X#param_x2 Y#param_y2 F1
/	o<#self_id0> endif

	o<poly_add_item> CALL [-2] [#param_x1] [#param_y1] [#param_dir] [#param_cs] [#param_cr] [#param_rev] [100] [#param_x2] [#param_y2] [#param_arc_h]
o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `0` |
| | **"Link"** | | |
| 3 | "Type" | Dropdown | `0` |
| 4 | "Radius" | Float | `0.3000` |
| 5 | "Complement" | Toggle | `0` |
| | **"Connection"** | | |
| 7 | "Type" | Dropdown | `1` |
| 8 | "Arc height" | Float | `1.0000` |
| | **"Mirror line"** | | |
| 10 | "X1" | Float | `-10.0000` |
| 11 | "Y1" | Float | `0.0000` |
| 12 | "X2" | Float | `10.0000` |
| 13 | "Y2" | Float | `0.0000` |
| 14 | "Show line" | Toggle | `1` |

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

### "Type"
- **NGC variable**: `#param_dir`
- "Type"
- **Options**: "Straight line=1:Arc clockwise=2:Arc counter-clockwise=3"

### "Arc height"
- **NGC variable**: `#param_arc_h`
- "Arc height"
- **Min**: 0  **Max**: 999999.9  **Digits**: 4

### "X1"
- **NGC variable**: `#param_x1`
- "Line start"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y1"
- **NGC variable**: `#param_y1`
- "Line start"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X2"
- **NGC variable**: `#param_x2`
- "Line end"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y2"
- **NGC variable**: `#param_y2`
- "Line end"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Show line"
- **NGC variable**: `#param_show`
- "Show mirror line"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(mirror polyline items author : Fernand Veilleux)
o<#self_id_active> if [#<in_polyline> AND #param_act AND [#5000 GE 1] AND [[#param_x1 NE #param_x2] OR [#param_y1 NE #param_y2]]]
/	o<#self_id0> if [#param_show]
/		o<#self_id1> if [#<_has_z_axis>]
/			G0 X#param_x1 Y#param_y1 Z#<surface>
/		o<#self_id1> else
/			G0 X#param_x1 Y#param_y1
/		o<#self_id1> endif
/		G1 X#param_x2 Y#param_y2 F1
/	o<#self_id0> endif

	o<poly_add_item> CALL [-2] [#param_x1] [#param_y1] [#param_dir] [#param_cs] [#param_cr] [#param_rev] [100] [#param_x2] [#param_y2] [#param_arc_h]
o<#self_id_active> endif
(end #sub_name)
```
