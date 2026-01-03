from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    urdf = os.path.join(
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

        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{"robot_description": open(urdf).read()}]
        ),

        Node(
            package="controller_manager",
            executable="ros2_control_node",
            parameters=[{"robot_description": open(urdf).read()},
                        controllers],
            output="screen"
        ),

        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_state_broadcaster"]
        ),

        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["diff_drive_controller"]
        )
    ])
