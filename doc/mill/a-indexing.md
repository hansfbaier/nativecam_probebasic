# "A indexing"

>"<b>Rotate A axis</b>"

| | |
|---|---|
| Type | `index-A` |
| Icon | `axis-a.png` |
| Source | `mill/index-axisA.cfg` |

## Subroutine

- **NGC**: ``

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `0` |
| | **"Parameters"** | | |
| 3 | "Number of steps" | Integer | `4` |
| 4 | "Start angle" | Float | `0.00` |
| 5 | "Fill angle" | Float | `360.00` |
| 6 | "Items" | items | `` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Disabling will NOT disable items"

### "Number of steps"
- **NGC variable**: `#param_num`
- "Number of steps"

### "Start angle"
- **NGC variable**: `#param_start`
- "Angle of the first item"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Fill angle"
- **NGC variable**: `#param_fill`
- "Angle covered by all items"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 2

### "Items"
- **NGC variable**: `#param_items`
- "Items"

## G-code Template

### Before (preamble)

```ngc
(begin #sub_name)
(indexing of A axis author : Fernand Veilleux)

o<#self_id_active_before> if [#param_act]

	o<#self_id_fill> if [[[#param_fill MOD 360] NE 0] AND [#param_num GT 1]]
		#<fill#ID> = [#param_fill * #param_num / [#param_num - 1]]
	o<#self_id_fill> else
		#<fill#ID> = #param_fill
	o<#self_id_fill> endif

	#<count#ID> = 0
	#<step#ID> = [#<fill#ID> / #param_num]

	o<#self_id_repeat> repeat [#param_num]
		G0 A[#param_start + #<step#ID> * #<count#ID>]

o<#self_id_active_before> endif

		(begin #sub_name items)
```

### After (postamble)

```ngc
(end #sub_name items)

o<#self_id_active_after> if [#param_act]
		#<count#ID> = [#<count#ID> + 1]
	o<#self_id_repeat> endrepeat

	G0 A0

o<#self_id_active_after> endif
(end #sub_name)
```
