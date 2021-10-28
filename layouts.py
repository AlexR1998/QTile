from libqtile import layout
from design import colors,margin

lay_config={"border_focus":colors[1],
            "border_width":2,
            "margin":margin,
            "border_normal":colors[0]
        }

layouts = [
    layout.Columns(**lay_config),
    layout.Matrix(**lay_config),
    layout.Max(**lay_config),
    layout.MonadTall(**lay_config),
    layout.MonadWide(**lay_config),

    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]