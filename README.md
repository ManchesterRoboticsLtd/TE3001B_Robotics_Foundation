<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/ManchesterRoboticsLtd/TE3001B_Fundamentals_of_Robotics/blob/main/Misc/Logos/Logotipo%20Vertical%20Bco_Transparente.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/ManchesterRoboticsLtd/TE3001B_Fundamentals_of_Robotics/blob/main/Misc/Logos/Logotipo%20Vertical%20Azul%20transparente.png">
  <img alt="Shows ITESM logo in black or white." width="160" align="right">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/ManchesterRoboticsLtd/TE3001B_Fundamentals_of_Robotics/blob/main/Misc/Logos/MCR2_Logo_White.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/ManchesterRoboticsLtd/TE3001B_Fundamentals_of_Robotics/blob/main/Misc/Logos/MCR2_Logo_Black.png">
  <img alt="Shows MCR2 logo in black or white." width="150" align="right">
</picture>

---
# TE3001B: Robotics Foundation

  ## Introduction
   * This course, developed by Manchester Robotics ltd. (MCR2), introduces the basic concepts and general knowledge of the ROS environment to the user.
   * The course is divided into five session, carefully designed for the user to learn about the different aspects of ROS  from topics and messages to control and simulation using ROS.
   * This course will be based on challenges to make the student aware of ROS basics and ROS communication with hardware.
   * This branch contains all the presentations, activities and files required for the “TE3001B: Fundamentación de Robótica” course of the Tec de Monterrey.
   * This repository is organised by sessions, each subfolder contains all the neccesary files for each one of the activities of this course.
   
## General Information
* Duration 5 Weeks
* Classes: Monday and Thursday  (1 – 2 PM) / 5 Weeks
* Starts: 13 February.
* Ends: 17 March
* ZOOM Link Classes: https://itesm.zoom.us/j/4779422764
 
## General Requirements
General requirements. Please be aware that a set of requirements especific for each session will be shown in each session subsection (Some items may be repeated).
* Computer with access to Zoom (online classes).
* Computer with Ubuntu 18.04 and ROS Melodic or MCR2 virtual machine (installation instructions in the presentation MCR2_VM_ROS).
* Knowledge of Windows. 
* Basic knowledge of Ubuntu (recommended).
* Basic understanding of robotics (recommended).
* Access to Hackerboard and a MCR2 DC motor. 
  * In case you have no access to the Hackeborad, the hardware can be replaced for an Arduino Mega, a L298n Motor Driver and a DC motor brushed with encoder (More information MCR2_General_Information_Prerequisites).
  <br/><br/><br/>
  <picture>
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/ManchesterRoboticsLtd/TE3001B_Fundamentals_of_Robotics/blob/main/Misc/Logos/Hardware.png">
  <img alt="Shows Hardware required." width="650" align="center">
</picture>
<br/><br/>

## Weekly Sessions

  ### Week 1: (Intorduction)
  This week will introduce the teaching team and the basics of ROS.
  #### Session 1:
  * Who we are? Introduction to MCR2.
  * Introduction to Robotics
  * Introduction to VM, Ubuntu
  #### Session 2:
  * Introduction to ROS
  * Overview of the ROS Environment: Topics, messages, ROS.
  * Activity 1 (Talker and Listener)
  * Launch files
  *	Activity 2: Launch Files
  * Q&A
  
  **Mini challenge:** Generate a node that send a signal to another node to process it.
  
  **Requirements:** Computer with access to Zoom, Ubuntu 18.04 and ROS Melodic Installed (Full installation). In case Ubuntu 18.04 cannot be installed, MCR2 offers a Virtual Machine with ROS preinstalled (installation instructions in Week 1 Folder).
  
  ### Week 2: (ROS Practicalities)  
  This week will introduce some useful ROS practicalities.
  #### Session 1:
  * ROS Namespaces
  * ROS Parameter Server
  * Activity 1: Parametrise previous nodes
  * ROS Custom Messages
  #### Session 2:
  * Control Basics: Continuous time only/ no theory just practicalities.
  * Q&A
  
  **Mini challenge:**: P/PI Controller from scratch to a 1st order simulated system.
  
  **Requirements:** Requirements of Session 1.

  ### Week 3: ROS-Hardware Communication
  This week will introduce hardware communication between ROS and the Hackerboard using ROSSerial.
  #### Session 1:
  * Motor Control Theory
  * ROS Serial
  * Arduino
  * ROS Serial/Arduino Communication.
  
  **Mini challenge:** Motor Speed regulation using ROS.
  #### Session 2:
  * Q&A Session.
  
  **Requirements:** Requirements of Session 1, Installation of the Arduino IDE and the Rosserial package in the VM or Ubuntu (See instructions on Session2 MCR2_Arduino_IDE_Confirguration), Access to Hackerboard and a MCR2 DC motor.
    * In case you have no access to the Hackeborad, the hardware can be replaced for an Arduino Mega, a L298n Motor Driver and a DC motor brushed with encoder (More information MCR2_General_Information_Prerequisites).
  
  ### Week 4: ROS Data Acquisition
  This week will introduce how to acquire data between ROS and the Hackerboard using ROSSerial.
  #### Session 1:
  * Encoder Basic Theory
  
  **Mini challenge:** Acquire data from the encoders using Arduino.
  
  **Challenge:**: PID Controller using ROS and compare with simulation.
  
  #### Session 2:
  * Q&A Session.
  
  **Requirements:** Requirements of Session 1 and Session 3.
  
  ### Week 5: Final Challenge
  Final Challenge presentation week.
  #### Session 1:
  * Q&A Session.
  #### Session 2:
  * Final Challenge.
  
  **Requirements:** Requirements of Session 1 and Session 3.
