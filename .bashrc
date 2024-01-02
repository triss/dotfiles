# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

# don't put duplicate lines in the history. See bash(1) for more options
# don't overwrite GNU Midnight Commander's setting of `ignorespace'.
HISTCONTROL=$HISTCONTROL${HISTCONTROL+:}ignoredups
# ... or force ignoredups and ignorespace
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# make less more friendly for non-text input files, see lesspipe(1)
#[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "$debian_chroot" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
# force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

red='\[\e[0;31m\]'
RED='\[\e[1;31m\]'
blue='\[\e[0;34m\]'
BLUE='\[\e[1;34m\]'
cyan='\[\e[0;36m\]'
CYAN='\[\e[1;36m\]'
green='\[\e[0;32m\]'
GREEN='\[\e[1;32m\]'
yellow='\[\e[0;33m\]'
YELLOW='\[\e[1;33m\]'
PURPLE='\[\e[1;35m\]'
purple='\[\e[0;35m\]'
nc='\[\e[0m\]'

if [ "$UID" = 0 ]; then
    PS1="$red\u$nc@$red\H$nc:$CYAN\w$nc\\n$red#$nc "
else
    PS1="$PURPLE\u$nc@$CYAN\H$nc:$GREEN\w$nc\\n$GREEN\$$nc "
fi
# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# some more ls aliases
alias ll='ls -lh'
alias la='ls -A'
alias l='ls -CF'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# Default parameter to send to the "less" command
# -R: show ANSI colors correctly; -i: case insensitive search
LESS="-R -i"

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
    . /etc/bash_completion
fi

# Add sbin directories to PATH.  This is useful on systems that have sudo
echo $PATH | grep -Eq "(^|:)/sbin(:|)"     || PATH=$PATH:/sbin
echo $PATH | grep -Eq "(^|:)/usr/sbin(:|)" || PATH=$PATH:/usr/sbin

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

#AVL-MXE TERMINAL CUSTOMIZATION

# DEFINE TEXT COLORS

# declare -r BLACK='\e[0;30m'
# declare -r RED='\e[0;31m'
# declare -r GREEN='\e[0;32m'
# declare -r BROWN='\e[0;33m'
# declare -r BLUE='\e[0;34m'
# declare -r PURPLE='\e[0;35m'
# declare -r CYAN='\e[0;36m'
# declare -r LIGHT_GREY='\e[0;37m'
# declare -r DARK_GREY='\e[0;90m'
# declare -r LIGHT_RED='\e[0;91m'
# declare -r LIGHT_GREEN='\e[0;92m'
# declare -r YELLOW='\e[0;93m'
# declare -r LIGHT_BLUE='\e[0;94m'
# declare -r LIGHT_PURPLE='\e[0;95m'
# declare -r LIGHT_CYAN='\e[0;96m'
# declare -r WHITE='\e[0;97m'
#
# # DEFINE BOLD TEXT COLOR
#
# declare -r BOLD_DARK_GREY='\e[1;30m'
# declare -r BOLD_LIGHT_RED='\e[1;31m'
# declare -r BOLD_LIGHT_GREEN='\e[1;32m'
# declare -r BOLD_YELLOW='\e[1;33m'
# declare -r BOLD_LIGHT_BLUE='\e[1;34m'
# declare -r BOLD_LIGHT_PURPLE='\e[1;35m'
# declare -r BOLD_LIGHT_CYAN='\e[1;36m'
# declare -r BOLD_WHITE='\e[1;37m'
#
# # DEFINE UNDERLINED TEXT
#
# declare -r UNDERLINE_BLACK='\e[4;30m'
# declare -r UNDERLINE_RED='\e[4;31m'
# declare -r UNDERLINE_GREEN='\e[4;32m'
# declare -r UNDERLINE_BROWN='\e[4;33m'
# declare -r UNDERLINE_BLUE='\e[4;34m'
# declare -r UNDERLINE_PURPLE='\e[4;35m'
# declare -r UNDERLINE_CYAN='\e[4;36m'
# declare -r UNDERLINE_LIGHT_GREY='\e[4;37m'

function setTextStyle() { echo -en "$1"; }

export CDP_SOUND_EXT=wav

# Todo.txt
export TODOTXT_DEFAULT_ACTION=ls
alias t='todo.sh'
source todo_completion
complete -F _todo t

setTextStyle $BROWN
#cat /opt/ASCII/AVL-MXE-Small.txt
pyfiglet --color=yellow:black Hello Tristan
echo "ヽ(⌐■_■)ノ♪♬"
setTextStyle $DEFAULT_TEXT
