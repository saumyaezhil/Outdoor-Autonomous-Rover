from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
import os

def generate_launch_description():

    urdf_path = os.path.join(
        os.getenv("HOME"),
        "outdoor_rover_ws/src/rover_description/urdf/rover.urdf"
    )

    return LaunchDescription([

        ExecuteProcess(
            cmd=["gazebo", "--verbose", "-s", "libgazebo_ros_factory.so"],
            output="screen"
        ),

        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{"robot_description": open(urdf_path).read()}],
            output="screen"
        ),

        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=["-entity", "rover", "-topic", "robot_description"],
            output="screen"
        ),

        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_state_broadcaster"],
            output="screen"
        ),

        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["diff_drive_controller"],
            output="screen"
        ),
    ])
