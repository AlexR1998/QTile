from libqtile import bar, widget
from libqtile.config import Screen
from libqtile import qtile
from design import colors,margin

widget_defaults = dict(
    font='Cantarell',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def volume():
    qtile.cmd_spawn("alacritty -e alsamixer")
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    background=colors[3],
                    foreground=colors[0]
                    ),
                widget.CurrentLayoutIcon(foreground=colors[1]),
                widget.GroupBox(
                    active=colors[1],
                    hide_unused=True,
                    block_highlight_text_color=colors[0],
                    this_current_screen_border=colors[3],
                    other_current_screen_border=colors[3],
                    other_screen_border=colors[3],
                    this_screen_border=colors[2],
                    highlight_method="block",
                    rounded=False,
                    margin_x=0,
                    padding_x=5,
                    padding_y=5,
                    borderwidth=1
                    ),
                widget.Spacer(),
                widget.Systray(),

                widget.TextBox(
                    font="Ubuntu Bold",
                    text="◀",
                    #text="◂",
                    foreground=colors[3],
                    background=colors[0],
                    padding=-2,
                    fontsize=23
                    ),
                widget.TextBox(
                    font="Ubuntu Bold",
                    text="",
                    fontsize=14,
                    foreground=colors[0],
                    background=colors[3],
                    mouse_callbacks={'Button1':volume}
                    ),
                widget.Volume(
                    foreground=colors[0],
                    background=colors[3],
                    padding=0,
                    margin=0
                    ),
                widget.TextBox(
                    font="Ubuntu Bold",
                    text="",
                    foreground=colors[0],
                    background=colors[3],
                    fontsize=14,
                    padding=5
                    ),
                widget.Battery(
                    unknown_char=' ',
                    format='{char}{percent:2.0%}',
                    foreground=colors[0],
                    background=colors[3],
                    padding=5,
                    charge_char="",
                    discharge_char="",
                    empty_char=""
                    ),
                widget.Clock(
                        format='%A %B %d, %I:%M %p',
                        foreground=colors[1],
                        background=colors[0],
                        padding=5
                        ),
                widget.QuickExit(
                        default_text="",
                        fontsize=14,
                        background=colors[1],
                        foreground=colors[0],
                        padding=5
                        ),
            ],
            20,
            opacity=0.9,
            margin=[margin,margin,0,margin]
        ),
    ),
]