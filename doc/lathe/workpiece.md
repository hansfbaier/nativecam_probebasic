# "Workpiece"

>"<b>Workpiece or raw material used</b>"

| | |
|---|---|
| Type | `workpiece` |
| Icon | `l-stock.png` |
| Source | `lathe/material.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(author : Fernand Veilleux)

G#param_wmode (Diameter = 7, Radius = 8)
#<_diameter_mode> = [#<_lathe_diameter_mode> + 1] (value is 1 for radius and 2 for diameter)

#<_wp_dia_od> = [#param_od / 2 * #<_diameter_mode>]
#<_wp_dia_id> = [#param_id / 2 * #<_diameter_mode>]

#<_x_rapid>  = [#param_x_rap * #<_diameter_mode>]
#<_z_rapid>  = #param_z_rap

/ o<#self_id1> if [#param_sh EQ 1]
	/ o<show_stock> CALL [#param_z] [#param_l]
/ o<#self_id1> endif

(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Show limits" | Toggle | `0` |
| | **"Size and coord"** | | |
| 3 | "Ext. diameter" | Float | `2.0000` |
| 4 | "Int. diameter" | Float | `0.0000` |
| 5 | "Length" | Float | `10.0000` |
| 6 | "Begin position" | Float | `0.0000` |
| | **"Params"** | | |
| 8 | "Work mode" | Dropdown | `7` |
| 9 | "Safe X rapid" | Float | `1.0000` |
| 10 | "Safe Z rapid" | Float | `1.0000` |

## Parameter Details

### "Show limits"
- **NGC variable**: `#param_sh`
- "Show limits"

### "Ext. diameter"
- **NGC variable**: `#param_od`
- "Ext. diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Int. diameter"
- **NGC variable**: `#param_id`
- "Only if hollow"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Length"
- **NGC variable**: `#param_l`
- "Length"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Begin position"
- **NGC variable**: `#param_z`
- "Z coord at tip"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Work mode"
- **NGC variable**: `#param_wmode`
- "Work mode"
- **Options**: "Diameter=7:Radius=8"

### "Safe X rapid"
- **NGC variable**: `#param_x_rap`
- "When job is done"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Safe Z rapid"
- **NGC variable**: `#param_z_rap`
- "When job is done"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(author : Fernand Veilleux)

G#param_wmode (Diameter = 7, Radius = 8)
#<_diameter_mode> = [#<_lathe_diameter_mode> + 1] (value is 1 for radius and 2 for diameter)

#<_wp_dia_od> = [#param_od / 2 * #<_diameter_mode>]
#<_wp_dia_id> = [#param_id / 2 * #<_diameter_mode>]

#<_x_rapid>  = [#param_x_rap * #<_diameter_mode>]
#<_z_rapid>  = #param_z_rap

/ o<#self_id1> if [#param_sh EQ 1]
	/ o<show_stock> CALL [#param_z] [#param_l]
/ o<#self_id1> endif

(end #sub_name)
```
