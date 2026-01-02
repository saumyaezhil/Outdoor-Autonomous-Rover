from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='topic_tools',
            executable='relay',
            name='lidar_relay',
            arguments=['/lidar_plugin/out', '/scan']
        ),

        Node(
            package='topic_tools',
            executable='relay',
            name='imu_relay',
            arguments=['/imu_plugin/out', '/imu/data']
        ),

        Node(
            package='topic_tools',
            executable='relay',
            name='gps_relay',
            arguments=['/gps_plugin/out', '/gps/fix']
        )
    ])
