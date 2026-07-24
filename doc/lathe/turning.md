# "Turning"

>"<b>External straight turning with optional radiuses</b>&#10;Uses compensation with a radius&#10;Cutter orientation should be 1, 2, 9 or None"

| | |
|---|---|
| Type | `turning` |
| Icon | `lathe-surface.png` |
| Source | `lathe/turning.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_act> if [#param_act]
	o<turning> CALL [#param_b_x] [#param_e_x] [#param_b_z] [#param_e_z] [#param_fin] [#param_r] [#param_ropt]
o<#self_id_act> endif

(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"X axis"** | | |
| 3 | "Begin diameter" | Float | `1.0000` |
| 4 | "End diameter" | Float | `0.8000` |
| | **"Z axis"** | | |
| 6 | "Begin" | Float | `0.0000` |
| 7 | "End" | Float | `-1.0000` |
| | **"Options"** | | |
| 9 | "End radius" | Dropdown | `1` |
| 10 | "Radius" | Float | `0.0000` |
| | **"Finishing"** | | |
| 12 | "Number of passes" | Integer | `1` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Begin diameter"
- **NGC variable**: `#param_b_x`
- "Begin diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "End diameter"
- **NGC variable**: `#param_e_x`
- "End diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Begin"
- **NGC variable**: `#param_b_z`
- "Begin"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "End"
- **NGC variable**: `#param_e_z`
- "End"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "End radius"
- **NGC variable**: `#param_ropt`
- "End radius"
- **Options**: "None w/ compensation=0:None w/o compensation=1:Full radius=2:Stop at Begin diameter=3"

### "Radius"
- **NGC variable**: `#param_r`
- "Less than cutter radius means no radius at end"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Number of passes"
- **NGC variable**: `#param_fin`
- "Or spring passes"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_act> if [#param_act]
	o<turning> CALL [#param_b_x] [#param_e_x] [#param_b_z] [#param_e_z] [#param_fin] [#param_r] [#param_ropt]
o<#self_id_act> endif

(end #sub_name)
```
