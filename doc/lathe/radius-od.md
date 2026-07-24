# "Radius OD"

>"<b>Create external radius using compensation.</b>&#10;Cutter orientation should be 1, 2, 9 or None"

| | |
|---|---|
| Type | `radius_od` |
| Icon | `corner-radius.png` |
| Source | `lathe/radius_od.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_act> if [#param_act]
	o<radius_od> CALL [#param_x] [#param_z] [#param_r] [#param_d] [#param_fin]
o<#self_id_act> endif

(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Crest"** | | |
| 3 | "Diameter" | Float | `1.0000` |
| 4 | "Z" | Float | `0.0000` |
| | **"Params"** | | |
| 6 | "Radius" | Float | `0.2500` |
| 7 | "Direction" | Dropdown | `0` |
| | **"Finishing"** | | |
| 9 | "Number of passes" | Integer | `1` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Diameter"
- **NGC variable**: `#param_x`
- "Diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Z"
- **NGC variable**: `#param_z`
- "Z"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Radius"
- **NGC variable**: `#param_r`
- "Radius"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Direction"
- **NGC variable**: `#param_d`
- "Choose from Begin to End"
- **Options**: "X- to Z-=0:Z+ to X-=1:Z- to X-=2:X- to Z+=3"

### "Number of passes"
- **NGC variable**: `#param_fin`
- "Or spring passes"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_act> if [#param_act]
	o<radius_od> CALL [#param_x] [#param_z] [#param_r] [#param_d] [#param_fin]
o<#self_id_act> endif

(end #sub_name)
```
