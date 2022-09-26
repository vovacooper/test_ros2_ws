#!/bin/bash
set -e

source /opt/ros/noetic/setup.bash
source /opt/ros/foxy/setup.bash

source ros2_ws/install/setup.bash

exec "$@"