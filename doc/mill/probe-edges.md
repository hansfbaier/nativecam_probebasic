# "Probe Edges"

>"<b>Probe Edges with touch-off options</b>&#10;When done, the probe will be above the edge"

| | |
|---|---|
| Type | `probe-edge` |
| Icon | `probe-edge.png` |
| Source | `mill/probe-edge.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(probe edge author : Fernand Veilleux)

o<#self_id_ena> if [#param_act]
	#<temp_z#ID> = #<_z>

	o<#self_id_X> if [#param_axis EQ 0]
		o<probe> call [#param_dir] [0] [0]
		o<#self_id_Xup> if [#param_dir GT 0]
			#<x#ID> = [#5061 + #<_probe_tip_dia> / 2]
			G0 X[#5061 - #<_probe_tip_dia>]
		o<#self_id_Xup> else
			#<x#ID> = [#5061 - #<_probe_tip_dia> / 2]
			G0 X[#5061 + #<_probe_tip_dia>]
		o<#self_id_Xup> endif
		G0 Z[#<temp_z#ID> + #param_clr]
		G0 X[#<x#ID>]
		o<#self_id_Xt> if [#param_touch]
			G10 L20 P#5220 X0
		o<#self_id_Xt> endif
	o<#self_id_X> endif

	o<#self_id_Y> if [#param_axis EQ 1]
		o<probe> call [0] [#param_dir] [0]
		o<#self_id_Yup> if [#param_dir GT 0]
			#<y#ID> = [#5062 + #<_probe_tip_dia> / 2]
			G0 Y[#5062 - #<_probe_tip_dia>]
		o<#self_id_Yup> else
			#<y#ID> = [#5062 - #<_probe_tip_dia> / 2]
			G0 Y[#5062 + #<_probe_tip_dia>]
		o<#self_id_Yup> endif
		G0 Z[#<temp_z#ID> + #param_clr]
		G0 Y[#<y#ID>]

		o<#self_id_Yt> if [#param_touch]
			G10 L20 P#5220 Y0
		o<#self_id_Yt> endif
	o<#self_id_Y> endif

o<#self_id_ena> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Options"** | | |
| 3 | "Axis" | Dropdown | `0` |
| 4 | "Direction" | Dropdown | `1` |
| 5 | "Clear Z" | Float | `0.5000` |
| 6 | "Touch off axis" | Toggle | `1` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Axis"
- **NGC variable**: `#param_axis`
- "Select axis to find edge"
- **Options**: "X=0:Y=1"

### "Direction"
- **NGC variable**: `#param_dir`
- "Direction"
- **Options**: "Ascending=1:Descending=-1"

### "Clear Z"
- **NGC variable**: `#param_clr`
- "To raise above workpiece"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Touch off axis"
- **NGC variable**: `#param_touch`
- "Set axis to 0"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(probe edge author : Fernand Veilleux)

o<#self_id_ena> if [#param_act]
	#<temp_z#ID> = #<_z>

	o<#self_id_X> if [#param_axis EQ 0]
		o<probe> call [#param_dir] [0] [0]
		o<#self_id_Xup> if [#param_dir GT 0]
			#<x#ID> = [#5061 + #<_probe_tip_dia> / 2]
			G0 X[#5061 - #<_probe_tip_dia>]
		o<#self_id_Xup> else
			#<x#ID> = [#5061 - #<_probe_tip_dia> / 2]
			G0 X[#5061 + #<_probe_tip_dia>]
		o<#self_id_Xup> endif
		G0 Z[#<temp_z#ID> + #param_clr]
		G0 X[#<x#ID>]
		o<#self_id_Xt> if [#param_touch]
			G10 L20 P#5220 X0
		o<#self_id_Xt> endif
	o<#self_id_X> endif

	o<#self_id_Y> if [#param_axis EQ 1]
		o<probe> call [0] [#param_dir] [0]
		o<#self_id_Yup> if [#param_dir GT 0]
			#<y#ID> = [#5062 + #<_probe_tip_dia> / 2]
			G0 Y[#5062 - #<_probe_tip_dia>]
		o<#self_id_Yup> else
			#<y#ID> = [#5062 - #<_probe_tip_dia> / 2]
			G0 Y[#5062 + #<_probe_tip_dia>]
		o<#self_id_Yup> endif
		G0 Z[#<temp_z#ID> + #param_clr]
		G0 Y[#<y#ID>]

		o<#self_id_Yt> if [#param_touch]
			G10 L20 P#5220 Y0
		o<#self_id_Yt> endif
	o<#self_id_Y> endif

o<#self_id_ena> endif
(end #sub_name)
```
