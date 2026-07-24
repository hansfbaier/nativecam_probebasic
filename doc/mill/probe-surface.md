# "Probe Surface"

>"<b>Probe height of material and set value</b>"

| | |
|---|---|
| Type | `probe_surf` |
| Icon | `probe-down.png` |
| Source | `mill/probe-surface.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(probe z and set author : Fernand Veilleux)

o<#self_id_ena> if [#param_act]
	o<probe> call [0] [0] [#param_zdepth]
	G10 L20 P#5220 Z[#<probe_height>]
	G0 Z[#<probe_height> + #param_fo]
	o<#self_id0> if [#param_stop EQ 1]
		M2
	o<#self_id0> endif
o<#self_id_ena> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Params"** | | |
| 3 | "Max depth" | Float | `-1.0000` |
| 4 | "Final offset" | Float | `1.0000` |
| 5 | "End program" | Toggle | `1` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Max depth"
- **NGC variable**: `#param_zdepth`
- "Maximum depth before stopping"
- **Min**: -999999.9  **Max**: 0.0  **Digits**: 4

### "Final offset"
- **NGC variable**: `#param_fo`
- "Offset after setting"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "End program"
- **NGC variable**: `#param_stop`
- "End after reaching position"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(probe z and set author : Fernand Veilleux)

o<#self_id_ena> if [#param_act]
	o<probe> call [0] [0] [#param_zdepth]
	G10 L20 P#5220 Z[#<probe_height>]
	G0 Z[#<probe_height> + #param_fo]
	o<#self_id0> if [#param_stop EQ 1]
		M2
	o<#self_id0> endif
o<#self_id_ena> endif
(end #sub_name)
```
