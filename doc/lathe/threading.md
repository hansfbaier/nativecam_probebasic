# "Threading"

>"<b>External or internal thread, metric or imperial (Verify)</b>&#10;Cutter orientation should be 6 for external, 8 for internal or None"

| | |
|---|---|
| Type | `threading` |
| Icon | `threading.png` |
| Source | `lathe/threading.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_act> if [#param_act]
	o<select> CALL [31] [#param_sd] [#param_sdu] [-1] [#param_sdg]

	o<threading> CALL [#param_sz] [#param_ez] [#param_u] [#param_d] [#31] [#param_p] [#param_dgrs] [#param_id] [#param_pk] [#param_t] [#param_sc] [#param_ta] [#param_hc]
o<#self_id_act> endif

(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Coords"** | | |
| 3 | "Begin Z" | Float | `0.0000` |
| 4 | "End Z" | Float | `-1.0000` |
| | **"Thread definition"** | | |
| 6 | "Units" | Dropdown | `0` |
| 7 | "Major diameter" | Float | `0.8000` |
| 8 | "Minor diameter" | Dropdown (editable) | `1` |
| 9 |  | Float | `0.6300` |
| 10 |  | G-code | `` |
| 11 | "Pitch" | Float | `10.0000` |
| 12 | "Starts" | Integer | `1` |
| | **"Params"** | | |
| 14 | "Depth degression" | Float | `1.0000` |
| 15 | "Init thread depth" | Float | `0.0100` |
| 16 | "Thread peak" | Float | `0.0400` |
| 17 | "End taper" | Dropdown | `2` |
| 18 | "Taper angle" | Float | `30.00` |
| 19 | "Spring passes" | Integer | `2` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Active"

### "Begin Z"
- **NGC variable**: `#param_sz`
- "Begin Z"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "End Z"
- **NGC variable**: `#param_ez`
- "End Z"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Units"
- **NGC variable**: `#param_u`
- "Units"
- **Options**: "Imperial=0:Metric=1"

### "Major diameter"
- **NGC variable**: `#param_d`
- "Major diameter"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Minor diameter"
- **NGC variable**: `#param_sd`
- "Minor diameter"
- **Options**: "User defined=0:Automatic=1:G-Code=2"

### 
- **NGC variable**: `#param_sdu`
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### 
- **NGC variable**: `#param_sdg`

### "Pitch"
- **NGC variable**: `#param_p`
- "Metric pitch is thread to thread, imperial is per inch"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Starts"
- **NGC variable**: `#param_hc`
- "Number of helix"

### "Depth degression"
- **NGC variable**: `#param_dgrs`
- "1 = constant depth, 2 = constant area"
- **Min**: 1.0  **Max**: 3.0  **Digits**: 4

### "Init thread depth"
- **NGC variable**: `#param_id`
- "Depth of first pass in diameter measurement"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Thread peak"
- **NGC variable**: `#param_pk`
- "Positive for external, negative for internal"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "End taper"
- **NGC variable**: `#param_t`
- "End taper"
- **Options**: "None=0:On entry=1:On exit=2:Both=3"

### "Taper angle"
- **NGC variable**: `#param_ta`
- "Taper angle"
- **Min**: 15.0  **Max**: 60.0  **Digits**: 2

### "Spring passes"
- **NGC variable**: `#param_sc`
- "Spring passes"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(author : Fernand Veilleux)

o<#self_id_act> if [#param_act]
	o<select> CALL [31] [#param_sd] [#param_sdu] [-1] [#param_sdg]

	o<threading> CALL [#param_sz] [#param_ez] [#param_u] [#param_d] [#31] [#param_p] [#param_dgrs] [#param_id] [#param_pk] [#param_t] [#param_sc] [#param_ta] [#param_hc]
o<#self_id_act> endif

(end #sub_name)
```
