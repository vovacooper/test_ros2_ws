from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    ld = LaunchDescription()
    talker_node = Node(
        package='py_pubsub',
        namespace='py_pubsub',
        executable='talker',
        name='talker'
    )
    listener_node = Node(
        package='py_pubsub',
        namespace='py_pubsub',
        executable='listener',
        name='listener'
    )
    ld.add_action(talker_node)
    ld.add_action(listener_node)
    
    # TODO: add record bag

    return ld