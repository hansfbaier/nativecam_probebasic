# "Parting Off"

>"<b>Parting single or multiple pieces</b>&#10;Cutter orientation should be 6, 9 or None"

| | |
|---|---|
| Type | `parting` |
| Icon | `parting.png` |
| Source | `lathe/parting.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(author : Fernand Veilleux)
o<#self_id_act> if [#param_act]
	o<select>  CALL [42] [#param_b_z] [#param_b_zu] [#<_z>] [#param_b_zg]
	G0 X[#<_wp_dia_od> + #<_x_rapid>]
	M#<_cooling_mode>

	#<b_x#ID> = [#param_b_x / 2 * #<_diameter_mode>]
	#<e_x#ID> = [#param_e_x / 2 * #<_diameter_mode>]

	#<z#ID> = #param_ref
	o<#self_id1> repeat [#param_c]
		#<z#ID> = [#<z#ID> + #42 - [#param_ref]]
		G0 Z#<z#ID>
		G0 X#<b_x#ID>
		G1 X#<e_x#ID>
		G0 X[#<_wp_dia_od> + #<_x_rapid>]
	o<#self_id1> endrepeat

	M9 (cooling off)

o<#self_id_act> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"X axis"** | | |
| 3 | "Begin diameter" | Float | `1.0000` |
| 4 | "End diameter" | Float | `0.0000` |
| | **"Z axis"** | | |
| 6 | "Reference" | Float | `0.0000` |
| 7 | "First cut" | Dropdown (editable) | `0` |
| 8 |  | Float | `-1.0000` |
| 9 |  | G-code | `` |
| | **"Params"** | | |
| 11 | "Copies" | Integer | `1` |

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

### "Reference"
- **NGC variable**: `#param_ref`
- "Reference"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "First cut"
- **NGC variable**: `#param_b_z`
- "Will part at this position"
- **Options**: "User defined=0:Current position=1:G-Code=2"

### 
- **NGC variable**: `#param_b_zu`
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### 
- **NGC variable**: `#param_b_zg`

### "Copies"
- **NGC variable**: `#param_c`
- "Copies length will be 'First' minus 'Reference'"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(author : Fernand Veilleux)
o<#self_id_act> if [#param_act]
	o<select>  CALL [42] [#param_b_z] [#param_b_zu] [#<_z>] [#param_b_zg]
	G0 X[#<_wp_dia_od> + #<_x_rapid>]
	M#<_cooling_mode>

	#<b_x#ID> = [#param_b_x / 2 * #<_diameter_mode>]
	#<e_x#ID> = [#param_e_x / 2 * #<_diameter_mode>]

	#<z#ID> = #param_ref
	o<#self_id1> repeat [#param_c]
		#<z#ID> = [#<z#ID> + #42 - [#param_ref]]
		G0 Z#<z#ID>
		G0 X#<b_x#ID>
		G1 X#<e_x#ID>
		G0 X[#<_wp_dia_od> + #<_x_rapid>]
	o<#self_id1> endrepeat

	M9 (cooling off)

o<#self_id_act> endif
(end #sub_name)
```
