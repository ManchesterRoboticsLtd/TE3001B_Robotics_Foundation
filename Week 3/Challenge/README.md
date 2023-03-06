<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/ManchesterRoboticsLtd/TE3001B_Robotics_Foundation/blob/main/Misc/Logos/Logotipo%20Vertical%20Bco_Transparente.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/ManchesterRoboticsLtd/TE3001B_Robotics_Foundation/blob/main/Misc/Logos/Logotipo%20Vertical%20Azul%20transparente.png">
  <img alt="Shows ITESM logo in black or white." width="160" align="right">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/ManchesterRoboticsLtd/TE3001B_Robotics_Foundation/blob/main/Misc/Logos/MCR2_Logo_White.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/ManchesterRoboticsLtd/TE3001B_Robotics_Foundation/blob/main/Misc/Logos/MCR2_Logo_Black.png">
  <img alt="Shows MCR2 logo in black or white." width="150" align="right">
</picture>

# Week 3: MCR2 DC Motor Mini Challenge

* In this folder, the student will find the neccessary files for Mini challenge 3.
* The instruction for this challenge can be found inside the presentation *MCR2_MiniChallenge_3*

### << We Encourage the students to NOT USE the files and follow the instructions during class and in the presentation to make this activity !! >>

## Description
This mini challenge is intended for the student to review the concepts introduced in the previous sessions.

## Instructions

* Download the "*motor_control*" package into your *catkin_ws/src* folder.
* Open the launch folder and modify the port to be used (ttyUSB0 or ttyACM0 accordingly) inside "*motor.launch*" file
```
    <node name="motor" pkg="rosserial_python" type="serial_node.py">
    <param name="port"	type="string"	value="/dev/ttyUSB0"/>   
    </node>
```
* Modify the line 164 of the CMakeLists.txt with the name of your script e.g., scripts/foo.py

* Remember to change Port permissions in Ubuntu as shown in the presentation.
* Remember to make the nodes executable using the the following commands
```
 chmod +x foo.py
```

## Rules
  * This is challenge not a class. The students are encouraged to research, improve tune explain their algorithms by themselves.
  * MCR2(Manchester Robotics) Reserves the right to answer a question if it is determined that the questions contains partially or totally an answer.
  * The students are welcomed to ask only about the theoretical aspect of the classed.
  * No remote control or any other form of human interaction with the simulator or ROS is allowed (except at the start when launching the files).
  * It is forbidden to use any other internet libraires with the exception of standard libraires or NumPy.
  * If in doubt about libraires please ask any teaching assistant.
  * Improvements to the algorithms are encouraged and may be used as long as the students provide the reasons and a detailed explanation on the improvements.
  * All the students must be respectful towards each other and abide by the previously defined rules.
  * Manchester robotics reserves the right to provide any form of grading. Grading and grading methodology are done by the professor in charge of the unit.
  

