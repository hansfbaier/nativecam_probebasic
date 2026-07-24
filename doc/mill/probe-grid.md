# "Probe Grid"

>"<b>Probe Array of Points on stock and save to a file</b>"

| | |
|---|---|
| Type | `probe-array` |
| Icon | `probe-grid.png` |
| Source | `mill/probe-array.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(probe array author : Fernand Veilleux)

o<#self_id_active> if [#param_act]
	o<#self_id_rev0> if [#param_rev]
		#<_probe_latch> = -#<_probe_latch>
	o<#self_id_rev0> endif

	(probeopen,#param_fn)
	o<#self_id_ax> if [#param_dir]
		#<probe_Y> = [#<wp_front> + #param_dy / 2]
		o<#self_id_Y_loop> while [#<probe_Y> LT #<wp_rear>]
			#<probe_X> = [#<wp_left> + #param_dx / 2]
			o<#self_id_X_loop> while [#<probe_X> LT #<wp_right>]
				G0 Z[#<_rapid_z>]
				G0 X#<probe_X> Y#<probe_Y>
				o<probe> call [0] [0] [#param_depth]
				#<probe_X> = [#<probe_X> + #param_dx]
			o<#self_id_X_loop> endwhile
			#<probe_Y> = [#<probe_Y> + #param_dy]
		o<#self_id_Y_loop> endwhile

	o<#self_id_ax> else
		#<probe_X> = [#<wp_left> + #param_dx / 2]
		o<#self_id_X_loop1> while [#<probe_X> LT #<wp_right>]
			#<probe_Y> = [#<wp_front> + #param_dy / 2]
			o<#self_id_Y_loop1> while [#<probe_Y> LT #<wp_rear>]
				G0 Z[#<_rapid_z>]
				G0 X#<probe_X> Y#<probe_Y>
				o<probe> call [0] [0] [#param_depth]
				#<probe_Y> = [#<probe_Y> + #param_dy]
			o<#self_id_Y_loop1> endwhile
			#<probe_X> = [#<probe_X> + #param_dx]
		o<#self_id_X_loop1> endwhile
	o<#self_id_ax> endif
	(probeclose)
	G0 Z[#<_rapid_z>]

	o<#self_id_rev1> if [#param_rev]
		#<_probe_latch> = -#<_probe_latch>
	o<#self_id_rev1> endif

o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Probing and offsets"** | | |
| 3 | "File name" | string | `probe-results.txt` |
| 4 | "Depth" | Float | `-0.3000` |
| 5 | "Reverse latch dir" | Toggle | `0` |
| 6 | "dX" | Float | `0.2500` |
| 7 | "dY" | Float | `0.2500` |
| 8 | "Master" | Dropdown | `0` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "File name"
- **NGC variable**: `#param_fn`
- "Enter file name to save to"

### "Depth"
- **NGC variable**: `#param_depth`
- "Maximum depth"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Reverse latch dir"
- **NGC variable**: `#param_rev`
- "Reverse latch dir"

### "dX"
- **NGC variable**: `#param_dx`
- "X offset"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "dY"
- **NGC variable**: `#param_dy`
- "Y offset"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Master"
- **NGC variable**: `#param_dir`
- "Master axis to follow"
- **Options**: "X axis=0:Y axis=1"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(probe array author : Fernand Veilleux)

o<#self_id_active> if [#param_act]
	o<#self_id_rev0> if [#param_rev]
		#<_probe_latch> = -#<_probe_latch>
	o<#self_id_rev0> endif

	(probeopen,#param_fn)
	o<#self_id_ax> if [#param_dir]
		#<probe_Y> = [#<wp_front> + #param_dy / 2]
		o<#self_id_Y_loop> while [#<probe_Y> LT #<wp_rear>]
			#<probe_X> = [#<wp_left> + #param_dx / 2]
			o<#self_id_X_loop> while [#<probe_X> LT #<wp_right>]
				G0 Z[#<_rapid_z>]
				G0 X#<probe_X> Y#<probe_Y>
				o<probe> call [0] [0] [#param_depth]
				#<probe_X> = [#<probe_X> + #param_dx]
			o<#self_id_X_loop> endwhile
			#<probe_Y> = [#<probe_Y> + #param_dy]
		o<#self_id_Y_loop> endwhile

	o<#self_id_ax> else
		#<probe_X> = [#<wp_left> + #param_dx / 2]
		o<#self_id_X_loop1> while [#<probe_X> LT #<wp_right>]
			#<probe_Y> = [#<wp_front> + #param_dy / 2]
			o<#self_id_Y_loop1> while [#<probe_Y> LT #<wp_rear>]
				G0 Z[#<_rapid_z>]
				G0 X#<probe_X> Y#<probe_Y>
				o<probe> call [0] [0] [#param_depth]
				#<probe_Y> = [#<probe_Y> + #param_dy]
			o<#self_id_Y_loop1> endwhile
			#<probe_X> = [#<probe_X> + #param_dx]
		o<#self_id_X_loop1> endwhile
	o<#self_id_ax> endif
	(probeclose)
	G0 Z[#<_rapid_z>]

	o<#self_id_rev1> if [#param_rev]
		#<_probe_latch> = -#<_probe_latch>
	o<#self_id_rev1> endif

o<#self_id_active> endif
(end #sub_name)
```
