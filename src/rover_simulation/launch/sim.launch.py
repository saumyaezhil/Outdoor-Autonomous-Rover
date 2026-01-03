from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("gazebo_ros"),
                "launch",
                "gazebo.launch.py"
            )
        )
    )

    urdf_path = os.path.join(
        get_package_share_directory("rover_description"),
        "urdf",
        "rover.urdf"
    )

    controllers = os.path.join(
        get_package_share_directory("rover_simulation"),
        "config",
        "controllers.yaml"
    )

    return LaunchDescription([

        gazebo,

        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{"robot_description": open(urdf_path).read()}]
        ),

        # IMPORTANT: controllers are loaded INTO Gazebo's controller_manager
        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_state_broadcaster"],
            parameters=[controllers]
        ),

        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["diff_drive_controller"],
            parameters=[controllers]
        ),

        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=["-entity", "rover", "-file", urdf_path],
            output="screen"
        )
    ])
