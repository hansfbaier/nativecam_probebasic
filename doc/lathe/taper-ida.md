# "Taper IDA"

>"<b>Inside taper by angle and small/large diameter/radius</b>&#10;Cutter orientation should be 3, 9 or None"

| | |
|---|---|
| Type | `taper_ida` |
| Icon | `taper-ida.png` |
| Source | `lathe/taper_ida.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_act> if [#param_act]
	o<taper_id> CALL [#param_b_x] [#param_e_x] [#param_b_z] [#param_a] [#param_fin] [#param_pa]
o<#self_id_act> endif

(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"X axis"** | | |
| 3 | "Small diameter" | Float | `0.8000` |
| 4 | "Large diameter" | Float | `1.0000` |
| | **"Z axis"** | | |
| 6 | "Begin" | Float | `0.0000` |
| | **"Params"** | | |
| 8 | "Angle" | Float | `12.00` |
| 9 | "Path" | Dropdown | `0` |
| | **"Finishing"** | | |
| 11 | "Number of passes" | Integer | `1` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Small diameter"
- **NGC variable**: `#param_b_x`
- "Small diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Large diameter"
- **NGC variable**: `#param_e_x`
- "Large diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Begin"
- **NGC variable**: `#param_b_z`
- "End will be defined by angle"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Angle"
- **NGC variable**: `#param_a`
- "0 &#176; &lt; Angle &lt; 90 &#176;"
- **Min**: 0.0  **Max**: 90.0  **Digits**: 2

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
	o<taper_id> CALL [#param_b_x] [#param_e_x] [#param_b_z] [#param_a] [#param_fin] [#param_pa]
o<#self_id_act> endif

(end #sub_name)
```
