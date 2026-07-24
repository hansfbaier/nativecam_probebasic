# "Slot/oval 1 point"

>"<b>Creates a Slot from a single point</b>&#10;Reference point can be center of slot or of one end"

| | |
|---|---|
| Type | `slot` |
| Icon | `slot.png` |
| Source | `plasma/slot.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(slot from center or end author: Fernand Veilleux)
o<#self_id_active> if [#param_act] (if active)
	#<l#ID>   = [#param_l]
	#<w#ID>   = [#param_w]

	o<select> CALL [33] [#param_ref] [#<l#ID> / 2] [0]

	o<rectangle> CALL [#param_x] [#param_y] [#<l#ID> + #<w#ID>] [#<w#ID>] [#param_rot] [#33] [0] [1] [#<w#ID> / 2] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_pv]
o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords"** | | |
| 4 | "X" | Float | `0.0000` |
| 5 | "X axis align" | Dropdown | `0` |
| 6 | "Y" | Float | `0.0000` |
| | **"Size, rotation"** | | |
| 8 | "Width" | Float | `0.5000` |
| 9 | "Effective length" | Float | `1.0000` |
| 10 | "Rotation" | Float | `0.00` |
| | **"Cutting"** | | |
| 12 | "Option" | Dropdown | `0` |
| 13 | "Direction" | Dropdown | `3` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_pv`
- "Show design"

### "X"
- **NGC variable**: `#param_x`
- "X Center"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X axis align"
- **NGC variable**: `#param_ref`
- "X,Y center of slot or left end"
- **Options**: "End=0:Center of slot=1"

### "Y"
- **NGC variable**: `#param_y`
- "Y center"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Width"
- **NGC variable**: `#param_w`
- "Width of slot"
- **Min**: 0  **Max**: 999999.9  **Digits**: 4

### "Effective length"
- **NGC variable**: `#param_l`
- "Length between center of arcs"
- **Min**: 0  **Max**: 999999.9  **Digits**: 4

### "Rotation"
- **NGC variable**: `#param_rot`
- "Angle rotated"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Option"
- **NGC variable**: `#param_opt`
- "Select tool path"
- **Options**: "Inside=0:On the line=2:Outside=3"

### "Direction"
- **NGC variable**: `#param_dir`
- "Direction of tool path"
- **Options**: "Clockwise=2:Counter-Clockwise=3"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(slot from center or end author: Fernand Veilleux)
o<#self_id_active> if [#param_act] (if active)
	#<l#ID>   = [#param_l]
	#<w#ID>   = [#param_w]

	o<select> CALL [33] [#param_ref] [#<l#ID> / 2] [0]

	o<rectangle> CALL [#param_x] [#param_y] [#<l#ID> + #<w#ID>] [#<w#ID>] [#param_rot] [#33] [0] [1] [#<w#ID> / 2] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_pv]
o<#self_id_active> endif
(end #sub_name)
```
