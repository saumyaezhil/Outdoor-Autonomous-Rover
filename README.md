# Outdoor Autonomous Rover

This is a differential-drive rover project built on ROS 2 Humble. I'm taking a deliberate bottom-up approach here: get the control fundamentals working correctly before layering on navigation or sensors.

Right now the rover has a functioning `ros2_control` setup with a differential drive controller that's publishing odometry on `/diff_drive_controller/odom`. The joint state broadcaster is active, velocity commands work through `/cmd_vel`, and everything runs in Gazebo Classic using `gazebo_ros2_control`. I've verified both controllers are active and the topic structure is correct.

The URDF is intentionally barebones with no visual meshes, just `base_link` and two wheel joints with primitive collision shapes. I stripped out the mesh dependencies because they were adding complexity without helping me debug the control logic. The physics works, the odometry publishes, and the wheels respond to commands. That's what matters right now.

To build it, just run `colcon build --symlink-install` in your workspace. You can launch the control stack by itself with `ros2 launch rover_simulation control_only.launch.py` or fire up Gazebo with the simulation launch file. Check that controllers are running with `ros2 control list_controllers` and test velocity commands by publishing to `/cmd_vel`.

What's missing is pretty much everything above the control layer. No teleoperation yet, no Nav2, no sensors, no localization. I'll add teleoperation next so I can drive it around manually and validate the control response, then integrate a lidar, then build out the Nav2 stack. Visual meshes might come later if there's a reason for them, but right now they'd just be cosmetic.

The point is to have a stable foundation where each layer actually works before adding the next one. Too many robotics projects try to do everything at once and end up debugging navigation when the real problem is that the wheels aren't spinning right.
