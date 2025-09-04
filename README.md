TurtleBot3 Square Movement (ROS 2)

This is a ROS 2 package that makes a TurtleBot3 robot move in a square path using velocity commands.

Features

Publishes velocity commands to /cmd_vel

Makes the robot move in a square (forward → turn → forward → turn ...)

Written in Python

Requirements

ROS 2 Jazzy (or Humble/Foxy if modified)

TurtleBot3 simulation (Gazebo or RViz)

Python 3.12+

How to Run

Clone this package into your ROS 2 workspace:
cd ~/ros2_ws/src
git clone https://github.com/sanjana759/turtlebot3_square.git# TurtleBot3 SqTurtleBot3 Square Movement (ROS 2)

This is a ROS 2 package that makes a TurtleBot3 robot move in a square path using velocity commands.

Features

Publishes velocity commands to /cmd_vel

Makes the robot move in a square (forward → turn → forward → turn ...)

Written in Python

Requirements

ROS 2 Jazzy (or Humble/Foxy if modified)

TurtleBot3 simulation (Gazebo or RViz)

Python 3.12+

How to Run

Clone this package into your ROS 2 workspace:
cd ~/ros2_ws/src
git clone https://github.com/sanjana759/turtlebot3_square.gituare Movement (ROS 2)

Build the workspace:
cd ~/ros2_ws
colcon build
source install/setup.bash

Launch TurtleBot3 simulation (Gazebo):
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

Run the square movement node:
ros2 run turtlebot3_square square

Repository Structure

square.py → main Python node

launch/ → launch files

package.xml → package metadata

setup.py → Python entry points

Author

Sanjana Anchan

