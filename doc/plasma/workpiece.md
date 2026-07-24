# "Workpiece"

>"<b>Workpiece or Raw material used</b>"

| | |
|---|---|
| Type | `workpiece2` |
| Icon | `square.png` |
| Source | `plasma/material2d.cfg` |

## Subroutine

- **NGC**: `
(begin #sub_name)
(workpiece definition author : Fernand Veilleux)
#<wp_width>         = [#param_w]
#<wp_length>        = [#param_l]
#<wp_depth>         = [#param_d]
#<wp_wall>          = [#param_wt]
#<wp_corner_radius> = [#param_cr]
#<wp_inside_width>  = [#<wp_width> - #<wp_wall> * 2]
#<wp_inside_length> = [#<wp_length> - #<wp_wall> * 2]

#<wp_x> = #param_x
#<wp_y> = #param_y

o<select> CALL [31] [#param_alx] [#param_x] [#param_x - #<wp_length> / 2] [#param_x - #<wp_length>]
#<wp_left>  = #31
#<wp_right> = [#<wp_left> + #<wp_length>]

o<select> CALL [31] [#param_aly] [#param_y - #<wp_width>] [#param_y - #<wp_width> / 2] [#param_y]
#<wp_front> = #31
#<wp_rear>  = [#<wp_front> + #<wp_width>]

o<select> CALL [31] [#param_alz] [#param_z] [#param_z + #<wp_depth>]
#<surface>  = #31

#<bottom>   = [#<surface> - #<wp_depth>]

/	o<#self_id_active> if [#param_sh] (show active)
/		o<stock> CALL [#<wp_left>] [#<wp_right>] [#<wp_front>] [#<wp_rear>] [#<surface>] [#<bottom>] [#param_cl] [#<wp_corner_radius>] [#<wp_wall>]
/		G0 X#param_x Y#param_y
/		o<#self_id_has_Z_axis> if [#<_has_z_axis>]
/			G0 Z#<surface>
/		o<#self_id_has_Z_axis> endif
/	o<#self_id_active> endif
(end #sub_name)`

## Parameters

| # | Parameter | Type | Default |
|---|-----------|------|---------|
| 1 | "Show workpiece" | Toggle | `1` |
| | **"Size"** | | |
| 3 | "Width (X)" | Float | `40.0000` |
| 4 | "Height (Y)" | Float | `20.0000` |
| 5 | "Depth (Z)" | Float | `0.2500` |
| | **"Coords"** | | |
| 7 | "X" | Float | `0.0000` |
| 8 | "X axis align" | Dropdown | `0` |
| 9 | "Y" | Float | `0.0000` |
| 10 | "Y axis align" | Dropdown | `2` |
| 11 | "Z" | Float | `0.0000` |
| 12 | "Z axis align" | Dropdown | `0` |
| | **"Options"** | | |
| 14 | "Corner radius" | Float | `0.0000` |
| 15 | "Wall thickness" | Float | `0.0000` |
| 16 | "Centerline align" | Dropdown | `2` |

## Parameter Details

### "Show workpiece"
- **NGC variable**: `#param_sh`
- "Show workpiece"

### "Width (X)"
- **NGC variable**: `#param_l`
- "X axis"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Height (Y)"
- **NGC variable**: `#param_w`
- "Y axis"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Depth (Z)"
- **NGC variable**: `#param_d`
- "Z axis"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "X"
- **NGC variable**: `#param_x`
- "X0"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "X axis align"
- **NGC variable**: `#param_alx`
- "Define X reference"
- **Options**: "Left=0:Center=1:Right=2"

### "Y"
- **NGC variable**: `#param_y`
- "Y0"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Y axis align"
- **NGC variable**: `#param_aly`
- "Define Y reference"
- **Options**: "Top=0:Center=1:Bottom=2"

### "Z"
- **NGC variable**: `#param_z`
- "Surface"
- **Min**: -999999.9  **Max**: 999999.9  **Digits**: 4

### "Z axis align"
- **NGC variable**: `#param_alz`
- "Define Z reference"
- **Options**: "Top=0:Bottom=1"

### "Corner radius"
- **NGC variable**: `#param_cr`
- "Define radius"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Wall thickness"
- **NGC variable**: `#param_wt`
- "Define if hollow"
- **Min**: 0.0  **Max**: 999999.9  **Digits**: 4

### "Centerline align"
- **NGC variable**: `#param_cl`
- "Define orientation of centerline"
- **Options**: "X axis=0:Y axis=1:Z axis=2"

## G-code Template

### Call (main subroutine)

```ngc
(begin #sub_name)
(workpiece definition author : Fernand Veilleux)
#<wp_width>         = [#param_w]
#<wp_length>        = [#param_l]
#<wp_depth>         = [#param_d]
#<wp_wall>          = [#param_wt]
#<wp_corner_radius> = [#param_cr]
#<wp_inside_width>  = [#<wp_width> - #<wp_wall> * 2]
#<wp_inside_length> = [#<wp_length> - #<wp_wall> * 2]

#<wp_x> = #param_x
#<wp_y> = #param_y

o<select> CALL [31] [#param_alx] [#param_x] [#param_x - #<wp_length> / 2] [#param_x - #<wp_length>]
#<wp_left>  = #31
#<wp_right> = [#<wp_left> + #<wp_length>]

o<select> CALL [31] [#param_aly] [#param_y - #<wp_width>] [#param_y - #<wp_width> / 2] [#param_y]
#<wp_front> = #31
#<wp_rear>  = [#<wp_front> + #<wp_width>]

o<select> CALL [31] [#param_alz] [#param_z] [#param_z + #<wp_depth>]
#<surface>  = #31

#<bottom>   = [#<surface> - #<wp_depth>]

/	o<#self_id_active> if [#param_sh] (show active)
/		o<stock> CALL [#<wp_left>] [#<wp_right>] [#<wp_front>] [#<wp_rear>] [#<surface>] [#<bottom>] [#param_cl] [#<wp_corner_radius>] [#<wp_wall>]
/		G0 X#param_x Y#param_y
/		o<#self_id_has_Z_axis> if [#<_has_z_axis>]
/			G0 Z#<surface>
/		o<#self_id_has_Z_axis> endif
/	o<#self_id_active> endif
(end #sub_name)
```
