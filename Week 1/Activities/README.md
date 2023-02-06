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


# Week 1: Activities and Examples

In this folder, the student will find the files containing the solution for Activity 1.
### << We Encourage the students to NOT USE the files and follow the instructions during class and in the presentation to make this activity !! >>

### Requirements
* Ubuntu in VM or dual booting
* ROS installed
* Compile the files using catkin_make from terminal (from the catkin_ws folder)

## Activity 1 : Creating a Talker and Listener Nodes

<p align="center"><img src="https://user-images.githubusercontent.com/67285979/206562180-f12c6968-4585-405a-ba0d-9ef271c0b014.png" 
alt="ROS Basics" width="450" border="10"/></p>

* Create your package called "basic_comms” (the dependencies used are rospy and std_msgs
* Implement the code talker and listener code in Python.(This must be placed in the src folder of your package)
* Modify your Cmakelist.txt and the Package.xml file to include your code You can find help [here](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)
* Use some of the command tools to verify the correct functioning of the system. Hint: Go back to slides about the talker and the listener
* Use the following commands in different terminals to run and test your nodes independently.
```
roscore
rosrun basic_comms talker.py
rostopic echo /chatter
```
```
roscore
rosrun basic_comms listener.py
rostopic pub /chatter <tab complete>
```

  - Note: You do not need to modify the CMake (unless you need to use a non-standard library)
  - Remember to make the nodes executable using the the following command inside the *catkin_ws/src/basic_comms/src* folders 
```
 chmod +x talker.py
 chmod +x listener.py
```

## Activity 2
* Create a folder named *launch* inside the package *basic_comms*
* Create a *roslaunch* file i.e., *activity1.launch* for the previous nodes.
* Edit the code inside the file as shown in the presentation or in the *activity1.launch* file inside the folder *basic_comms* 
* Open a terminal an launch the nodes as follows

```
roslaunch basic_comms activity1.launch
```

