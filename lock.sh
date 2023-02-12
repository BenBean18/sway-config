#!/bin/sh

export XDG_RUNTIME_DIR=/run/user/1000
export WAYLAND_DISPLAY=wayland-1

BLANK='#00000000'
WHITE='#ffffffff'
IMAGEPATH='/usr/share/backgrounds/canvas_by_roytanck.jpg'
swaylock --inside-color=$BLANK        \
--ring-ver-color=$BLANK          \
--text-ver-color=$BLANK \
--text-wrong-color=$BLANK \
--ring-wrong-color=$BLANK          \
--ring-color=$BLANK \
--line-color=$WHITE \
--line-ver-color=$WHITE \
--inside-ver-color=$BLANK \
--inside-color=$BLANK \
--separator-color=$BLANK \
--key-hl-color=$WHITE \
-n \
--image=$IMAGEPATH \

# Put 
# #!/bin/sh
# #if [ "${1}" == "pre" ]; then
# #  # Do the thing you want before suspend here, e.g.:
#   su bean /home/bean/.config/sway/lock.sh & sleep 0.5
# #fi
# in /lib/systemd/system-sleep/lock.sh