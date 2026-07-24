# "Slot/oval 2 points"

>"<b>Creates a Slot between two end points</b>"

| | |
|---|---|
| Type | `slot-2points` |
| Icon | `slot-2.png` |
| Source | `plasma/slot-2.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(slot between two points author : Fernand Veilleux)
o<#self_id_active> if [#param_act] (if active)
	#<w#ID>   = [#param_w]

	o<line> CALL [#param_x1] [#param_y1] [#param_x2] [#param_y2]
		o<rectangle> CALL [#param_x1] [#param_y1] [#<_line_len> + #<w#ID>] [#<w#ID>] [#<_line_phi>] [#<_line_len> / 2] [0] [1] [#<w#ID> / 2] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_fc]
o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords, size"** | | |
| 4 | "X1" | Float | `0.0000` |
| 5 | "Y1" | Float | `0.0000` |
| 6 | "X2" | Float | `2.0000` |
| 7 | "Y2" | Float | `1.0000` |
| 8 | "Width" | Float | `0.5000` |
| | **"Cutting"** | | |
| 10 | "Option" | Dropdown | `0` |
| 11 | "Direction" | Dropdown | `3` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_fc`
- "Show design"

### "X1"
- **NGC variable**: `#param_x1`
- "First point"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y1"
- **NGC variable**: `#param_y1`
- "First point"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X2"
- **NGC variable**: `#param_x2`
- "Second point"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y2"
- **NGC variable**: `#param_y2`
- "Second point"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Width"
- **NGC variable**: `#param_w`
- "Width of slot"
- **Min**: 0  **Max**: 999999.9  **Digits**: 4

### "Option"
- **NGC variable**: `#param_opt`
- "Select tool path"
- **Options**: "Inside=0:On the line=2:Outside=3"

### "Direction"
- **NGC variable**: `#param_dir`
- "Direction of path"
- **Options**: "Clockwise=2:Counter-Clockwise=3"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(slot between two points author : Fernand Veilleux)
o<#self_id_active> if [#param_act] (if active)
	#<w#ID>   = [#param_w]

	o<line> CALL [#param_x1] [#param_y1] [#param_x2] [#param_y2]
		o<rectangle> CALL [#param_x1] [#param_y1] [#<_line_len> + #<w#ID>] [#<w#ID>] [#<_line_phi>] [#<_line_len> / 2] [0] [1] [#<w#ID> / 2] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_fc]
o<#self_id_active> endif
(end #sub_name)
```
