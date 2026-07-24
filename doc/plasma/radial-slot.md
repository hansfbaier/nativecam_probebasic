# "Radial Slot"

>"<b>Creates a Radial Slot</b>&#10;Define center, start and extend angle"

| | |
|---|---|
| Type | `slot-arc` |
| Icon | `radial-slot.png` |
| Source | `plasma/slot-arc.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(radial slot author : Fernand Veilleux)
o<#self_id_active> if [#param_act] (if active)
	o<slot_arc> CALL [#param_cx] [#param_cy] [#param_r] [#param_w] [#param_strt] [#param_ext] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_pv] [#param_es]
o<#self_id_active> endif`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords"** | | |
| 4 | "cX" | Float | `0.0000` |
| 5 | "cY" | Float | `0.0000` |
| | **"Size"** | | |
| 7 | "Width" | Float | `0.3750` |
| 8 | "Radius" | Float | `1.5000` |
| | **"Start, extend"** | | |
| 10 | "Start angle" | Float | `10.00` |
| 11 | "Extend angle" | Float | `45.00` |
| 12 | "Ends style" | Dropdown | `0` |
| | **"Cutting"** | | |
| 14 | "Option" | Dropdown | `0` |
| 15 | "Direction" | Dropdown | `3` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_pv`
- "Show design"

### "cX"
- **NGC variable**: `#param_cx`
- "Center of slot arc"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "cY"
- **NGC variable**: `#param_cy`
- "Center of slot arc"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Width"
- **NGC variable**: `#param_w`
- "Width of slot"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Radius"
- **NGC variable**: `#param_r`
- "Distance from center"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Start angle"
- **NGC variable**: `#param_strt`
- "Absolute angle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Extend angle"
- **NGC variable**: `#param_ext`
- "Relative length of arc in degrees"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Ends style"
- **NGC variable**: `#param_es`
- "Ends style"
- **Options**: "Round=0:Converging=1"

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
(radial slot author : Fernand Veilleux)
o<#self_id_active> if [#param_act] (if active)
	o<slot_arc> CALL [#param_cx] [#param_cy] [#param_r] [#param_w] [#param_strt] [#param_ext] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_pv] [#param_es]
o<#self_id_active> endif
```
