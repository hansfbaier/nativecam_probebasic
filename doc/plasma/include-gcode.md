# "Include Gcode"

>"<b>Inserts a ngc file</b>"

| | |
|---|---|
| Type | `incl_gcode` |
| Icon | `file-gcode.png` |
| Source | `i_gcode.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_active> if [#param_act] (active)

	(CALL to included file #param_fname)
	o<#self_id_sub> CALL [#param_1] [#param_2] [#param_3] [#param_4] [#param_5] [#param_6]

o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `0` |
| | **"Selected file"** | | |
| 3 | "Gcode file" | filename | `` |
| | **"Parameters"** | | |
| 5 | "Parameter 1" | Float | `0.0000` |
| 6 | "Parameter 2" | Float | `0.0000` |
| 7 | "Parameter 3" | Float | `0.0000` |
| 8 | "Parameter 4" | Float | `0.0000` |
| 9 | "Parameter 5" | Float | `0.0000` |
| 10 | "Parameter 6" | Float | `0.0000` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Gcode file"
- **NGC variable**: `#param_fname`
- "Gcode file"

### "Parameter 1"
- **NGC variable**: `#param_1`
- "Parameter 1"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Parameter 2"
- **NGC variable**: `#param_2`
- "Parameter 2"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Parameter 3"
- **NGC variable**: `#param_3`
- "Parameter 3"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Parameter 4"
- **NGC variable**: `#param_4`
- "Parameter 4"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Parameter 5"
- **NGC variable**: `#param_5`
- "Parameter 5"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Parameter 6"
- **NGC variable**: `#param_6`
- "Parameter 6"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_active> if [#param_act] (active)

	(CALL to included file #param_fname)
	o<#self_id_sub> CALL [#param_1] [#param_2] [#param_3] [#param_4] [#param_5] [#param_6]

o<#self_id_active> endif
(end #sub_name)
```

### Definitions

```ngc
(included gcode file #param_fname)
o<#self_id_sub> sub
	<eval>self.include( "#param_fname" )</eval>

o<#self_id_sub> endsub
(end of #param_fname)
```
