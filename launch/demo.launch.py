from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import ThisLaunchFileDir

def generate_launch_description():

    ld = LaunchDescription()
    node_py_pub=Node(
        package='py_pub',
        # namespace='lulav',
        executable='talker',
        name='talker',
        remappings=[('topic', '/talker')],
        parameters=[{'my_str':'vova talker', 'my_int': 77, 'my_double_array': [4.4, 5.5, 6.6]}]                      
    )
    ld.add_action(node_py_pub)

    node_py_sub=Node(
        package='py_sub',
        # namespace='lulav',
        executable='listener',
        name='listener',        
        # parameters=[{'name_param':'vova listener'}]
    )
    ld.add_action(node_py_sub)
    return ld
    