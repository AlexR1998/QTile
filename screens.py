from libqtile import bar, widget
from libqtile.config import Screen
from libqtile import qtile
import design
from design import colors

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
                # widget.CurrentLayout(
                #     background=design.bar_backgrounds,
                #     foreground=design.bar_foregrounds
                #     ),
                #widget.CurrentLayoutIcon(foreground="#000000"),
                widget.GroupBox(
                    active=design.bar_foregrounds,
                    hide_unused=True,
                    block_highlight_text_color=design.bar_foregrounds,
                    this_current_screen_border=design.borders,
                    highlight_method="line",
                    rounded=False,
                    margin_x=0,
                    padding_x=8,
                    padding_y=8,
                    borderwidth=3,
                    background="#000000",
                    fontsize=14,
                    font='Cantarell Bold'
                    ),
                widget.Spacer(),
                
                widget.NvidiaSensors(
                        font='Cantarell Bold',
                        fontsize=14,
                        background=design.borders
                        
                ),




                widget.Clock(
                        format='%d/%m/%y %H:%M',
                        foreground=design.bar_foregrounds,
                        #background=design.borders,
                        padding=5,
                        fontsize=14,
                        font='Cantarell Bold'
                        ),
                


                widget.Systray(),

                
                # widget.QuickExit(
                #         default_text="",
                #         fontsize=25,
                #         background=design.bar_backgrounds,
                #         foreground=design.bar_foregrounds,
                #         padding=8
                #         ),
            ],
            30,
            opacity=0.8,
            margin=[0,0,0,0]
        ),
    ),
]