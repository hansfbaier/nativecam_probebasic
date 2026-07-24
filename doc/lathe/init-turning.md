# "Init Turning"

>"<b>Initial turning to find X center</b>&#10;Position cutter where you want to begin"

| | |
|---|---|
| Type | `turning` |
| Icon | `od.png` |
| Source | `lathe/init-turning.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_act> if [#param_act]
	o<init_turning> CALL [#param_x] [#param_z] [#param_fin]
o<#self_id_act> endif

(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"End offsets"** | | |
| 3 | "X" | Float | `-0.0500` |
| 4 | "Z" | Float | `-0.5000` |
| | **"Finishing"** | | |
| 6 | "Number of passes" | Integer | `1` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "X"
- **NGC variable**: `#param_x`
- "X"
- **Min**: -999999.9  **Max**: 0.0  **Digits**: 4

### "Z"
- **NGC variable**: `#param_z`
- "Z"
- **Min**: -999999.9  **Max**: 0.0  **Digits**: 4

### "Number of passes"
- **NGC variable**: `#param_fin`
- "Or spring passes"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_act> if [#param_act]
	o<init_turning> CALL [#param_x] [#param_z] [#param_fin]
o<#self_id_act> endif

(end #sub_name)
```
