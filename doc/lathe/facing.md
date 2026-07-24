# "Facing"

>"<b>Face end and optionnaly set this face to 0.0</b>&#10; Verify cutter orientation"

| | |
|---|---|
| Type | `facing` |
| Icon | `lathe-facing.png` |
| Source | `lathe/facing.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_act> if [#param_act]
	o<select>  CALL [42] [#param_sz] [#param_zu_s] [#<_z>] [#param_zugc]

	o<facing> CALL [#param_b_x] [#param_e_x] [#42] [#42 + #param_lr] [#param_fin] [#param_t]

o<#self_id_act> endif

(end #sub_name)
`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"X axis"** | | |
| 3 | "Begin diameter" | Float | `1.0000` |
| 4 | "End diameter" | Float | `0.0000` |
| | **"Z axis"** | | |
| 6 | "Begin" | Dropdown (editable) | `1` |
| 7 |  | Float | `0.0000` |
| 8 |  | G-code | `` |
| 9 | "End offset" | Float | `-0.0300` |
| | **"Finishing"** | | |
| 11 | "Number of passes" | Integer | `1` |
| | **"Touch off"** | | |
| 13 | "Set Z to 0" | Toggle | `1` |

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
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Begin"
- **NGC variable**: `#param_sz`
- "Pre or user defined"
- **Options**: "User defined=0:Current position=1:G-Code=2"

### 
- **NGC variable**: `#param_zu_s`
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### 
- **NGC variable**: `#param_zugc`

### "End offset"
- **NGC variable**: `#param_lr`
- "Length to remove"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Number of passes"
- **NGC variable**: `#param_fin`
- "Or spring passes"

### "Set Z to 0"
- **NGC variable**: `#param_t`
- "Set finished face to Z0"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_act> if [#param_act]
	o<select>  CALL [42] [#param_sz] [#param_zu_s] [#<_z>] [#param_zugc]

	o<facing> CALL [#param_b_x] [#param_e_x] [#42] [#42 + #param_lr] [#param_fin] [#param_t]

o<#self_id_act> endif

(end #sub_name)
```
