# "Repeated"

>"<b>Repeat polyline items</b>"

| | |
|---|---|
| Type | `plinerepeat` |
| Icon | `poly-repeat-items.png` |
| Source | `plasma/polyline-repeat.cfg` |

## Subroutine

- **NGC**: ``

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Repeat" | Integer | `1` |
| 3 | "Items" | items | `` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Disabling will disable ALL items in group"

### "Repeat"
- **NGC variable**: `#param_num`
- "Number of repetition"

### "Items"
- **NGC variable**: `#param_items`
- "Add polyline items to repeat"

## G-code Template

### Before (preamble)

```ngc
(begin #sub_name)
(repeated polyline items author : Fernand Veilleux)
o<#self_id_active> if [#param_act]
	o<#self_id0> repeat [#param_num]

	(begin #sub_name items)
```

### After (postamble)

```ngc
(end #sub_name items)

	o<#self_id0> endrepeat
o<#self_id_active> endif
(end #sub_name)
```
