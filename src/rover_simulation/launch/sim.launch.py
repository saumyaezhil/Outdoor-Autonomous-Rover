from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('gazebo_ros'),
                'launch',
                'gazebo.launch.py'
            )
        ),
        launch_arguments={
            'world': os.path.join(
                get_package_share_directory('rover_simulation'),
                'worlds',
                'outdoor.world'
            )
        }.items()
    )

    urdf = os.path.join(
        get_package_share_directory('rover_description'),
        'urdf',
        'rover.urdf.xacro'
    )

    return LaunchDescription([

        # Start Gazebo WITH ROS factory (guaranteed)
        gazebo_launch,

        # Publish robot TF
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': Command(['xacro ', urdf])
            }]
        ),

        # Spawn robot into Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-topic', 'robot_description',
                '-entity', 'outdoor_rover'
            ],
            output='screen'
        )
    ])
