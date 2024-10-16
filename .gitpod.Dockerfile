FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
ENV DISPLAY=:99

# Install required packages
RUN apt-get update && apt-get install -y \
    sudo \
    xvfb \
    git \
    unzip \
    patch \
    libncurses5-dev \
    libncursesw5-dev \
    libgtk2.0-dev \
    libxml2-dev \
    libudev-dev \
    libiw-dev \
    libsdl1.2-dev \
    lib32z1 \
    build-essential \
    daemontools \
    net-tools \
    nano \
    gcc-multilib

# Start Xvfb when the container starts
CMD sudo Xvfb :99 -screen 0 1024x768x16 & \
    export DISPLAY=:99 && \
    tail -f /dev/null