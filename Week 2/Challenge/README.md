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

# Week 2: Mini challenge

* In this folder, the student will find the neccessary files for Mini challenge 2.
* The instruction for this challenge can be found inside the presentation *MCR2_MiniChallenge_2*

### << We Encourage the students to NOT USE the files and follow the instructions during class and in the presentation to make this activity !! >>

## Description
This mini challenge is intended for the student to review the concepts introduced in the previous sessions.
* The activity consists of creating a controller for a simple first order system (/system) in ROS. 
* The system represents the dynamical behaviour of a DC Motor.
* The “/system” node, and a simple program structure (not mandatory) are provided by MCR2.
* The controller can be  “P”, “PI” or “PID” controller (other controllers can be accepted upon agreement with the professor.). 


<p align="center"><img src="https://user-images.githubusercontent.com/67285979/218272859-0c94088b-0727-4794-adab-621ee8fdf528.png" 
alt="ROS Basics" width="400" border="10"/></p>


## Instructions

* Download the "*pid_control*" package into your *catkin_ws/src* folder.
* Complete the node files *"controller.py"* and *"set_point_generator.py"* inside the *"scripts"* folder, according to the problem description and instructions.
* Complete the Roslaunch and msg files inside the *"launch"* and *"msg"* folder
* Execute the nodes using the *rosalunch* command.

  - Remember to make the nodes executable using the the following commands
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
  
  ## Expected results
  Left image shows the nodes and the topics that results from this challenge. 
  
  Right image shows the plot of the results (using *rqt_plot*) where the blue line represents the "motor_output" signal and the cyan line represent the "motor_input" signal.
  
  <p align="center"><img src="https://user-images.githubusercontent.com/67285979/218245460-c8f88bf0-65f1-4e5a-94d2-9a6bed2157a3.png" 
alt="ROS Basics" width="800" border="10"/></p>
