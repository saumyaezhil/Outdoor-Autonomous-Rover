# Outdoor Autonomous Rover

## Status
✅ Diff-drive rover
✅ ros2_control integrated
✅ diff_drive_controller running
✅ Odometry published on /diff_drive_controller/odom

## How to Run
```bash
colcon build --symlink-install
source install/setup.bash
ros2 launch rover_simulation control_only.launch.py
