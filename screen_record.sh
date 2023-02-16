#!/bin/bash
is_recording=$(pgrep wf-recorder)
if [ $is_recording ]
then
    pkill wf-recorder
else
    wf-recorder -f ~/Videos/"$(date +"%Y-%m-%d_%I-%M-%S_%p")".mkv &
fi