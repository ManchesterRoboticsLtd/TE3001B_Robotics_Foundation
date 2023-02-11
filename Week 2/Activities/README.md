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

# Week 2: Activities and Examples

In this folder, the student will find the files containing the solution for Activity 1.
### << We Encourage the students to NOT USE the files and follow the instructions during class and in the presentation to make this activity !! >>

### Requirements
* Ubuntu in VM or dual booting
* ROS installed
* Compile the files using catkin_make from terminal (from the catkin_ws folder)

## Activity 1 : Namespaces
<p align="center"><img src="https://user-images.githubusercontent.com/67285979/218240259-d277e45b-7d44-4ba2-8b47-6da4d4d3255c.png" 
alt="ROS Basics" width="450" border="10"/></p>

* Open the launch file of the previous Talker and Listener Example (activity1.launch).
* Modify it as follows
```
<?xml version="1.0" ?>
<launch>
	<group ns = "Group1">
<node name="talker" pkg="basic_comms" type="talker.py" output="screen"    launch-prefix="gnome-terminal --command" />

<node name="listener" pkg="basic_comms" type="listener.py" output="screen" launch-prefix="gnome-terminal --command" />    
	</group>    

	<group ns = "Group2">
node name="talker" pkg="basic_comms" type="talker.py" output="screen" launch-prefix="gnome-terminal --command" />        

<node name="listener" pkg="basic_comms" type="listener.py" output="screen" launch-prefix="gnome-terminal --command" />    
	</group>

</launch>

```

* Execute the Launch file
```
$ roslaunch basic_comms activity1.launch
```

* Execute the following command in a new terminal
```
$ rostopic list
```
* In a new terminal, execute the rqt_graph to visualise the nodes
```
$ rosrun rqt_graph rqt_graph
```


## Activity 2 : Parameters
<p align="center"><img src="https://user-images.githubusercontent.com/67285979/218240369-77d2d127-f807-4d8d-a260-a069a41e7f35.png" 
alt="ROS Basics" width="450" border="10"/></p>

<p align="center"><img src="https://user-images.githubusercontent.com/67285979/218240379-015fa626-1293-474e-b35f-e892bbe92a7a.png" 
alt="ROS Basics" width="450" border="10"/></p>


## Activity 3 : Parameter Files

<p align="center"><img src="https://user-images.githubusercontent.com/67285979/218240441-528f007a-e6b4-444b-80b1-69a10149f6b6.png" 
alt="ROS Basics" width="250" border="10"/></p>



## Activity 4 : Custom Messages
<p align="center"><img src="https://user-images.githubusercontent.com/67285979/218240617-48e882ee-f746-494b-bf64-62299897c5e4.png" 
alt="ROS Basics" width="350" border="10"/></p>


