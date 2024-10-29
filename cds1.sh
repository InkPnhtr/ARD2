#!/bin/bash
# Navigate through the directories




nohup x11vnc -display :99 -nopw -forever -shared &
export DISPLAY=:99
nohup ./ARDrone_SDK_2_0_1/Examples/Linux/Build/Release/noVNC/utils/novnc_proxy --vnc localhost:5900 --listen 6080 &
ps aux | grep Xvfb

cd ARDrone_SDK_2_0_1
cd Examples
cd Linux
cd Build
cd Release
