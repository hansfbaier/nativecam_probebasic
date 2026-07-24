# "Circle 2 points"

>"<b>Create a Circle by defining ends of diameter</b>&#10;Points are the ends of the diameter and can add a flat"

| | |
|---|---|
| Type | `circle-2` |
| Icon | `circle-2.png` |
| Source | `plasma/circle-2.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(circle from ends of diameter author : Fernand Veilleux)
o<#self_id_active> if [#param_act] (if active)
	#<flat#ID> = [#param_f]
	#<delx#ID> = [#param_x2 - #param_x1]
	#<dely#ID> = [#param_y2 - #param_y1]
	#<diameter#ID> = [SQRT[#<delx#ID> * #<delx#ID> + #<dely#ID> * #<dely#ID>]]
	#<cx#ID> = [[#param_x1 + #param_x2] / 2]
	#<cy#ID> = [[#param_y1 + #param_y2] / 2]

	o<circle> CALL [#<cx#ID>] [#<cy#ID>] [#<diameter#ID>] [#<flat#ID>] [#param_rot] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_fcut]
o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Show design" | Toggle | `1` |
| | **"Coords"** | | |
| 4 | "X1" | Float | `0.0000` |
| 5 | "Y1" | Float | `0.0000` |
| 6 | "X2" | Float | `2.0000` |
| 7 | "Y2" | Float | `1.0000` |
| | **"D flat"** | | |
| 9 | "Remove" | Float | `0.0000` |
| 10 | "Rotation" | Float | `0.00` |
| | **"Cutting"** | | |
| 12 | "Option" | Dropdown | `0` |
| 13 | "Direction" | Dropdown | `3` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Show design"
- **NGC variable**: `#param_fcut`
- "Show design"

### "X1"
- **NGC variable**: `#param_x1`
- "One end of the diameter"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y1"
- **NGC variable**: `#param_y1`
- "One end of the diameter"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X2"
- **NGC variable**: `#param_x2`
- "Opposite end of the diameter"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y2"
- **NGC variable**: `#param_y2`
- "Opposite end of the diameter"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Remove"
- **NGC variable**: `#param_f`
- "Height to remove from diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Rotation"
- **NGC variable**: `#param_rot`
- "Rotation of flat"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Option"
- **NGC variable**: `#param_opt`
- "Select tool path"
- **Options**: "Inside=0:On the line=2:Outside=3"

### "Direction"
- **NGC variable**: `#param_dir`
- "Direction of path"
- **Options**: "Clockwise=2:Counter-Clockwise=3"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(circle from ends of diameter author : Fernand Veilleux)
o<#self_id_active> if [#param_act] (if active)
	#<flat#ID> = [#param_f]
	#<delx#ID> = [#param_x2 - #param_x1]
	#<dely#ID> = [#param_y2 - #param_y1]
	#<diameter#ID> = [SQRT[#<delx#ID> * #<delx#ID> + #<dely#ID> * #<dely#ID>]]
	#<cx#ID> = [[#param_x1 + #param_x2] / 2]
	#<cy#ID> = [[#param_y1 + #param_y2] / 2]

	o<circle> CALL [#<cx#ID>] [#<cy#ID>] [#<diameter#ID>] [#<flat#ID>] [#param_rot] [#param_opt] [#param_dir] [#<pl_cut_start>] [#<surface>] [#<bottom>] [#param_fcut]
o<#self_id_active> endif
(end #sub_name)
```
