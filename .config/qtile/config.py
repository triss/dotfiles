from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from color import colors

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "control"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    # Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "e", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "Tab", lazy.spawn("rofi -show window"), desc="Switch windows"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(),
        desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r",
        lazy.spawn("rofi -modi combi -combi-modi window,run,drun -show combi"),
        desc="Spawn a command"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus=colors["red"],
        border_focus_stack=colors["red"],
        border_normal=colors["bg"],
        border_normal_stack=colors["bg"],
        border_width=5),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    # font="Ubuntu Nerd Font",
    fontsize=18,
    padding=3,
    foreground=colors["fg"],
    background=colors["green"]
)
extension_defaults = widget_defaults.copy()


def right_sep(color):
    return widget.TextBox(
        u'\ue0b0 ',
        background=colors["bg"],
        foreground=colors[color],
        padding=0,
        fontsize=24
    )


def left_sep(color):
    return widget.TextBox(
        u' \ue0b2',
        background=colors["bg"],
        foreground=colors[color],
        padding=0,
        fontsize=24
    )


screens = [
    Screen(
        wallpaper='~/Downloads/207891740_10167334451735206_3669207951917389381_n.jpg',
        wallpaper_mode='fill',
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    highlight_method='block',
                    active=colors["fg"],
                    background=colors["yellow"]
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]
        ),
    ),
    Screen(
        wallpaper='~/Downloads/207891740_10167334451735206_3669207951917389381_n.jpg',
        wallpaper_mode='fill',
        bottom=bar.Bar(
            [
                left_sep("pink"),
                widget.GroupBox(
                    highlight_method='block',
                    borderwidth=0,
                    rounded=False,
                    active=colors["fg"],
                    inactive=colors["fg_gutter"],
                    background=colors["pink"],
                    foreground=colors["green"],
                    other_screen_border=colors["cyan"],
                    other_current_screen_border=colors["cyan"],
                    this_current_screen_border=colors["pink"],
                    this_screen_border=colors["pink"],
                    urgent_border=colors["red"]
                ),
                right_sep("pink"),

                left_sep("green"),
                widget.WindowName(),
                right_sep("green"),

                widget.Systray(
                    background=colors["bg"]
                ),

                left_sep("yellow"),
                widget.GenPollCommand(
                    background=colors["yellow"],
                    foreground=colors["black"],
                    cmd="todo.sh -p lsp t",
                    shell=True,
                    padding=7
                ),
                right_sep("yellow"),

                widget.GenPollCommand(
                    background=colors["bg"],
                    fontsize=24,
                    cmd="cat ~/.jack_status",
                    shell=True,
                    padding=7
                ),

                left_sep("green"),
                widget.Pomodoro(
                    color_active=colors["fg"],
                    color_break=colors["yellow"],
                    color_inactive=colors["red"],
                    background=colors["fg_gutter"]
                ),
                right_sep("green"),

                left_sep("magenta"),
                widget.Clock(
                    format="%a %d %b %I:%M%p",
                    foreground=colors["bg"],
                    background=colors["magenta"]
                ),
                right_sep("magenta"),
            ],
            30,
            border_width=[7, 0, 7, 0],  # Draw top and bottom borders
            border_color=colors["bg"]
        )
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an client
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
wmname = "LG3D"
