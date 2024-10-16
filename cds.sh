#!/bin/bash



# Navigate through the directories

cd ARDrone_SDK_2_0_1
cd Examples
cd Linux
cd Build
cd Release

Xvfb :99 -screen 0 1024x768x16 &
export DISPLAY=:99
ps aux | grep Xvfb