# Custom Agents

This workspace contains two specialized agents for the agricultural robotics thesis project: an outdoor simulation agent for Gazebo and a navigation agent for ROS2/Nav2.

## `gazebo-robotics-simulator`
Use this agent for Gazebo simulation work:
- building outdoor field environments for precision agriculture
- creating or editing Husky or custom URDF/SDF robot models
- adding simulated sensors for crop and soil data acquisition
- tuning terrain, lighting, physics, and sensor realism

Example prompts:
- "Create a Gazebo world for an agricultural field with crop rows and irregular terrain"
- "Build a Husky-based robot model with multispectral camera, GNSS, and LiDAR sensors"
- "Add realistic lighting and unstructured obstacles for outdoor simulation"

## `ros2-navigation-dev`
Use this agent for ROS2 and Navigation2 work:
- creating ROS2 packages, nodes, launch files, and parameters
- integrating Navigation2 with the robot
- implementing coverage paths, obstacle avoidance, and motion control
- debugging navigation behavior in simulation missions

Example prompts:
- "Set up Nav2 for the Husky to run coverage missions in simulation"
- "Implement a custom planner for agricultural row traversal"
- "Create a ROS2 launch file for map server, planner, controller, and recovery behaviors"

## Notes
- The agents are stored in `.github/agents/` so they are workspace-specific.
- Reload VS Code if they do not appear immediately in the agent picker.
- These definitions are tuned to your thesis: autonomous outdoor robotic platform for precision agriculture, simulated only.
