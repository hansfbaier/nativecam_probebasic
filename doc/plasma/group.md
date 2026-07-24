# "Group"

>"<b>Group items together</b>"

| | |
|---|---|
| Type | `group` |
| Icon | `group.png` |
| Source | `group.cfg` |

## Subroutine

- **NGC**: ``

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| 2 | "Note" | Text | `` |
| 3 | "Items" | items | `` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_act`
- "Disabling will disable ALL items"

### "Note"
- **NGC variable**: `#param_n`
- "Note"

### "Items"
- **NGC variable**: `#param_0`
- "Items to group"

## G-code Template

### Before (preamble)

```ngc
(begin #sub_name)
(regular group authors : Nick Drobchenko and Fernand Veilleux)
o<#self_id_active> if [#param_act]

	(begin #sub_name items)
```

### After (postamble)

```ngc
(end #sub_name items)

o<#self_id_active> endif
(end #sub_name)
```
