# "GCode"

>"<b>Add gcode</b>&#10;lines will be parsed as usual so you can use &lt;eval>&lt;/eval>, '\\n'"

| | |
|---|---|
| Type | `g-code` |
| Icon | `gcode.png` |
| Source | `gcode.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(custom gcode lines author : Fernand Veilleux)

o<#self_id_active> if [#param_ena]
#param_gc
o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Active" | Toggle | `1` |
| | **"Lines"** | | |
| 3 | "GCode" | gc-lines | `` |

## Parameter Details

### "Active"
- **NGC variable**: `#param_ena`
- "Disabling will exclude lines"

### "GCode"
- **NGC variable**: `#param_gc`
- "Gcode line"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(custom gcode lines author : Fernand Veilleux)

o<#self_id_active> if [#param_ena]
#param_gc
o<#self_id_active> endif
(end #sub_name)
```
