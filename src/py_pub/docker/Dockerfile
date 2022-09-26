# This is an auto generated Dockerfile for ros:ros1-bridge
# generated from docker_images_ros2/ros1_bridge/create_ros_ros1_bridge_image.Dockerfile.em
FROM ros:foxy-ros-base-focal

# setup sources.list
RUN echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros1-latest.list

# setup keys
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

ENV ROS2_DISTRO foxy

# install ros2 packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-foxy-ros1-bridge=0.9.6-1* \
    ros-foxy-demo-nodes-cpp=0.9.3-1* \
    ros-foxy-demo-nodes-py=0.9.3-1* \
    && rm -rf /var/lib/apt/lists/*

# install and config cycloneDDS
RUN  apt-get update && apt install -y ros-foxy-rmw-cyclonedds-cpp
ENV  RMW_IMPLEMENTATION rmw_cyclonedds_cpp

WORKDIR /home/lulav/ros2_sim/

COPY / ros2_ws/src/py_pub/

RUN cd ros2_ws && \ 
    colcon build --merge-install --symlink-install --cmake-args '-DCMAKE_BUILD_TYPE=RelWithDebInfo' '-DCMAKE_EXPORT_COMPILE_COMMANDS=On' -Wall -Wextra -Wpedantic

COPY docker/ros_entrypoint.sh /
RUN chmod +x /ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["ros2", "run", "py_pub", "talker"]
# CMD ["bash"]
