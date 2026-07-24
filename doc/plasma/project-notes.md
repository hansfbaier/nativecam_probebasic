# "Project Notes"

>"<b>Shows project name and you can add a comment</b>"

| | |
|---|---|
| Type | `comment` |
| Icon | `prj-desc.png` |
| Source | `proj_desc.cfg` |

## Subroutine

- **NGC**: `
#param_n`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Project name" | prjname | `` |
| 2 | "Note" | Text | `` |

## Parameter Details

### "Project name"
- **NGC variable**: `#param_pn`
- "Project name"

### "Note"
- **NGC variable**: `#param_n`
- "Note"

## G-code Template

### Call (main subroutine)

```ngc
#param_n
```
