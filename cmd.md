
ros2 pkg executables [package_name]

ros2 pkg executables py_pub

ros2 pkg xml py_sub

# get all packages:
colcon list

colcon graph
colcon graph --legend

# get info:
colcon info py_sub




# Build
colcon build

# Source
source install/setup.sh 

# Launch
ros2 launch launch/demo.launch.py 



# HELP:
ros2 topic echo /talker
ros2 topic pub /talker std_msgs/String "data: HeHlllo ROS Developers"

# Check comunication
ros2 multicast send
ros2 multicast receive 
