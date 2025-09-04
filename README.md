# TurtleBot3 Square Movement (ROS 2)

This is a ROS 2 package that makes a TurtleBot3 robot move in a square path using velocity commands.

## Features
- Publishes velocity commands to `/cmd_vel`
- Makes the robot move in a square (forward → turn → forward → turn ...)
- Written in Python

## Requirements
- ROS 2 Jazzy (or Humble/Foxy if modified)
- TurtleBot3 simulation (Gazebo or RViz)
- Python 3.12+

## How to Run

1. Clone this package into your ROS 2 workspace:
   ```bash
   cd ~/ros2_ws/src
   git clone https://github.com/sanjana759/turtlebot3_square.git
