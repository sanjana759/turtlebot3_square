from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot3_square',
            executable='square',
            name='square_mover',
            output='screen',
        )
    ])
