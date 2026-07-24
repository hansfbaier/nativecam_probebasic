# "Cutting Params"

>"<b>Add cutting parameters</b>&#10;Changes setting accordingly even if disabled"

| | |
|---|---|
| Type | `cut_params2` |
| Icon | `torch.png` |
| Source | `plasma/cutting-params2d.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(changed params and kerf changing code author : Fernand Veilleux)
#<_feed_normal>     = #param_feed
#<_feed_vertical>   = #param_vfeed
#<pl_cut_start>     = #param_cutstart

#<_z_clear>         = #param_zcl
#<_rapid_z>         = [#<surface> + #<_z_clear> + #param_rap]
#<_in_kerf_factor>  = #param_s
#<_out_kerf_factor> = #param_f
#<_pierce_delay>    = #param_delay

o<#self_id_act> if [#param_act AND [#param_tnum NE #5400]]
	T#param_tnum M6
o<#self_id_act> endif
F#<_feed_normal>
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Cut"** | | |
| 3 | "Kerf width" | tool | `0` |
| 4 | "Start height" | Float | `0.1000` |
| 5 | "Lead in factor" | Float | `2.0000` |
| 6 | "Lead out factor" | Float | `1.5000` |
| 7 | "Pierce delay" | Float | `0.2500` |
| | **"Feed"** | | |
| 9 | "Normal feed" | Float | `10.0000` |
| 10 | "Vertical feed" | Float | `10.0000` |
| | **"Rapid params"** | | |
| 12 | "Rapid (Z)" | Float | `0.1000` |
| 13 | "Z clear" | Float | `0.2000` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Cutting params will be set even if disabled"

### "Kerf width"
- **NGC variable**: `#param_tnum`
- "Select kerf width for compensation"

### "Start height"
- **NGC variable**: `#param_cutstart`
- "Above surface"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Lead in factor"
- **NGC variable**: `#param_s`
- "Times kerf"
- **Min**: 0.501  **Max**: 999999.9  **Digits**: 4

### "Lead out factor"
- **NGC variable**: `#param_f`
- "Times kerf"
- **Min**: 0.501  **Max**: 999999.9  **Digits**: 4

### "Pierce delay"
- **NGC variable**: `#param_delay`
- "Wait after torch OK"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Normal feed"
- **NGC variable**: `#param_feed`
- "Normal feed"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Vertical feed"
- **NGC variable**: `#param_vfeed`
- "Vertical feed"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Rapid (Z)"
- **NGC variable**: `#param_rap`
- "Above Z clear"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Z clear"
- **NGC variable**: `#param_zcl`
- "Above cut start"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(changed params and kerf changing code author : Fernand Veilleux)
#<_feed_normal>     = #param_feed
#<_feed_vertical>   = #param_vfeed
#<pl_cut_start>     = #param_cutstart

#<_z_clear>         = #param_zcl
#<_rapid_z>         = [#<surface> + #<_z_clear> + #param_rap]
#<_in_kerf_factor>  = #param_s
#<_out_kerf_factor> = #param_f
#<_pierce_delay>    = #param_delay

o<#self_id_act> if [#param_act AND [#param_tnum NE #5400]]
	T#param_tnum M6
o<#self_id_act> endif
F#<_feed_normal>
(end #sub_name)
```
