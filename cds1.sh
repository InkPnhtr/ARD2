#!/bin/bash
# Navigate through the directories
nohup Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99
nohup fluxbox &
ps aux | grep Xvfb

nohup x11vnc -display :99 -nopw -forever -shared &
nohup ./ARDrone_SDK_2_0_1/Examples/Linux/Build/Release/noVNC/utils/novnc_proxy --vnc localhost:5900 --listen 6080 &
