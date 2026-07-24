# "Taper ODL"

>"<b>Machine a taper by length, small and large diameter</b>&#10;Cutter orientation should be 1, 2, 9 or None"

| | |
|---|---|
| Type | `taper_odl` |
| Icon | `taper-odl.png` |
| Source | `lathe/taper_odl.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_act> if [#param_act]
	o<line> CALL [#param_e_z] [-#param_b_x / 2] [#param_b_z] [-#param_e_x / 2]

	o<taper> CALL [#param_b_x] [#param_e_x] [#param_b_z] [#<_line_phi>] [#param_fin] [#param_pa]
o<#self_id_act> endif

(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"X axis"** | | |
| 3 | "Large diameter" | Float | `1.0000` |
| 4 | "Small diameter" | Float | `0.9000` |
| | **"Z axis"** | | |
| 6 | "Small diameter" | Float | `0.0000` |
| 7 | "Large diameter" | Float | `-1.0000` |
| | **"Params"** | | |
| 9 | "Path" | Dropdown | `0` |
| | **"Finishing"** | | |
| 11 | "Number of passes" | Integer | `1` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Large diameter"
- **NGC variable**: `#param_b_x`
- "Large diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Small diameter"
- **NGC variable**: `#param_e_x`
- "Small diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Small diameter"
- **NGC variable**: `#param_b_z`
- "Small diameter"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Large diameter"
- **NGC variable**: `#param_e_z`
- "Large diameter"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Path"
- **NGC variable**: `#param_pa`
- "Path"
- **Options**: "Follow drive line=0:Angular=1"

### "Number of passes"
- **NGC variable**: `#param_fin`
- "Or spring passes"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_act> if [#param_act]
	o<line> CALL [#param_e_z] [-#param_b_x / 2] [#param_b_z] [-#param_e_x / 2]

	o<taper> CALL [#param_b_x] [#param_e_x] [#param_b_z] [#<_line_phi>] [#param_fin] [#param_pa]
o<#self_id_act> endif

(end #sub_name)
```
