Fieldbot Gazebo model

Files created:
- model.config: sim/models/fieldbot/model.config
- model.sdf: sim/models/fieldbot/model.sdf
- world: sim/worlds/field_test.world

Notes & usage:
- The robot dimensions (meters) and masses follow your provided specs:
  - Base: 0.85 x 0.55 x 0.15 m, mass 15.78 kg (structure + battery)
  - Wheels: radius 0.165 m, width 0.13 m, mass 5.36 kg each (includes wheel, motor, bearings)
  - Track (left-right): 0.70 m
  - Wheelbase (front-back): 0.445 m

How to run in Gazebo (standalone Gazebo classic):

1) From the workspace root, export model path and start Gazebo world:

```bash
export GAZEBO_MODEL_PATH="$PWD/sim/models:${GAZEBO_MODEL_PATH:-}"
gazebo sim/worlds/field_test.world
```

2) To spawn the model via ros2 (if using `gazebo_ros`): publish the SDF or set GAZEBO_MODEL_PATH then use the world above. Alternatively, use `ros2 run gazebo_ros spawn_entity -file sim/models/fieldbot/model.sdf -entity fieldbot`.

Validation checklist:
- The robot appears on the ground plane centered at world origin.
- All four wheels are separate links and can be rotated by Gazebo joint controllers or plugins.

Next steps (optional):
- Add `ros2_control` transmissions and a `gazebo_ros2_control` plugin for controllers.
- Replace primitive visuals with meshes for realism (`meshes/` directory).
- Add sensors (IMU, lidar, cameras) and appropriate ROS2 topics/plugins.

ros2_control integration (added):

- Config file: `sim/config/fieldbot_controllers.yaml` contains example controller parameters for `joint_state_broadcaster` and `diff_drive_controller`.
- The model includes a `<ros2_control>` block and the `gazebo_ros2_control` plugin so the `controller_manager` inside Gazebo can claim joints.

Quick start (ROS 2 + Gazebo):

1) Start Gazebo with the world (in a terminal where your ROS2 environment is sourced):

```bash
export GAZEBO_MODEL_PATH="$PWD/sim/models:${GAZEBO_MODEL_PATH:-}"
ros2 launch gazebo_ros gazebo.launch.py world:=$(pwd)/sim/worlds/field_test.world
```

2) Spawn the robot if not included already:

```bash
ros2 run gazebo_ros spawn_entity -file sim/models/fieldbot/model.sdf -entity fieldbot
```

3) Load controllers (in another terminal with ROS2 sourced):

```bash
# spawn joint_state_broadcaster
ros2 run controller_manager spawner joint_state_broadcaster --controller-manager /controller_manager

# spawn diff_drive_controller
ros2 run controller_manager spawner diff_drive_controller --controller-manager /controller_manager
```

4) Publish velocity commands to `/cmd_vel` to drive the robot via the `diff_drive_controller`.

Notes:
- If `spawner` cannot connect, check the controller manager name at `/controller_manager` — the gazebo plugin should create it by that name.
- You may need to tune `wheel_separation` and `wheel_radius` in `sim/config/fieldbot_controllers.yaml` to match your needs.

If you want, I can add a ROS2 package with a launch file that starts Gazebo, spawns the robot and automatically spawns the controllers.

