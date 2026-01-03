# Outdoor Autonomous Rover

A differential-drive rover built with ROS 2 Humble and `ros2_control`. Right now it's all about getting the control basics right before adding navigation or fancy features.

## What Works

- ✓ Differential drive controller running
- ✓ Odometry publishing on `/diff_drive_controller/odom`
- ✓ Joint states broadcasting
- ✓ Gazebo simulation with `gazebo_ros2_control`
- ✓ Accepts velocity commands on `/cmd_vel`

## What Doesn't Work Yet

- Teleoperation (no keyboard/joystick control yet)
- Nav2 navigation stack
- Sensors (lidar, cameras, IMU)
- Any visual meshes (intentionally kept minimal for now)


## Why So Minimal?

I'm building this bottom-up. Get the control layer solid first, then add teleoperation, then sensors, then Nav2. No point debugging navigation if the wheels don't work right.

The URDF has no meshes because they were causing unnecessary complexity. Primitives work fine for getting the kinematics correct.

## Next Steps

1. Add teleop keyboard control
2. Integrate a lidar sensor
3. Set up Nav2
4. Maybe add visual meshes later if needed

## Dependencies

- ROS 2 Humble
- `ros2_control` and `diff_drive_controller`
- Gazebo Classic
