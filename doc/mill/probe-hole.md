# "Probe Hole"

>"<b>Probe a hole with options for touch-off center at 0.0&#10;START WITH PROBE IN CENTER OF HOLE AND DEPTH TO PROBE</b>"

| | |
|---|---|
| Type | `probe_hole` |
| Icon | `probe-hole.png` |
| Source | `mill/probe-hole.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(probe material author : Fernand Veilleux)

o<#self_id_ena> if [#param_act]
	o<probe_stock> CALL [0] [0] [0] [0] [0] [0] [#param_dbl] [#param_dbl] [1] [1] [#param_touch] [0] [#param_dia] [0] [#param_dia]

o<#self_id_ena> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Params"** | | |
| 3 | "Diameter" | Float | `1.0000` |
| 4 | "Double check" | Toggle | `0` |
| | **"Touch off"** | | |
| 6 | "Set origin" | Toggle | `1` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Diameter"
- **NGC variable**: `#param_dia`
- "Diameter"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Double check"
- **NGC variable**: `#param_dbl`
- "Measure twice"

### "Set origin"
- **NGC variable**: `#param_touch`
- "Set center to X0 and Y0"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(probe material author : Fernand Veilleux)

o<#self_id_ena> if [#param_act]
	o<probe_stock> CALL [0] [0] [0] [0] [0] [0] [#param_dbl] [#param_dbl] [1] [1] [#param_touch] [0] [#param_dia] [0] [#param_dia]

o<#self_id_ena> endif
(end #sub_name)
```
