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
This activity shows the usage of namespaces.

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
This activity shows the usage of parameters in launch files.
<p align="center"><img src="https://user-images.githubusercontent.com/67285979/218240369-77d2d127-f807-4d8d-a260-a069a41e7f35.png" 
alt="ROS Basics" width="450" border="10"/></p>

* Open the previous example Launch file  “activity1.launch”, and overwrite it as follows (you can rename it as "activity2.launch")
```
<?xml version="1.0" ?>
<launch>

<param name = "Message" value = "Manchester Robotics Global!" />

	<group ns = "Group1">
		<param name = "Message" value = "Manchester Robotics Local!" />
	
		<node name="talker" pkg="basic_comms" type="talker.py" output="screen" launch-prefix="gnome-terminal --command" >
		       <param name = "Message" value = "Manchester Robotics Private!" />
		</node>
		<node name="listener" pkg="basic_comms" type="listener.py" output="screen" launch-prefix="gnome-terminal --command" />
	</group>
	
	<group ns = "Group2">
		<param name = "Message" value = "Manchester Robotics Local!" />
		<node name="talker" pkg="basic_comms" type="talker.py" output="screen" launch-prefix="gnome-terminal --command" >
			<param name = "Message" value = "Manchester Robotics Private!" />
		</node>
		<node name="listener" pkg="basic_comms" type="listener.py" output="screen" launch-prefix="gnome-terminal --command" />
	</group>

</launch>
```
* Save the launch file and execute it as defined previously.
* You will see the parameters being displayed when ROS initializes

<p align="center"><img src="https://user-images.githubusercontent.com/67285979/218240379-015fa626-1293-474e-b35f-e892bbe92a7a.png" 
alt="ROS Basics" width="450" border="10"/></p>

* Open another terminal and type the following command to view the parameters in ROS
```
$ rosparam list
```
* To acces the parameter from a script, open the file “talker.py”
* Modify the line
```
 hello_str = “hello world %s” % rospy.get_time()
```
* For the following
```
 hello_str = rospy.get_param("/Message", "No Parameter Found")  + " " + str(rospy.get_time())
```
* Save the file and execute it using the roslaunch file

## Activity 3 : Parameter Files
This activity, shows the usage of parameter files.

<p align="center"><img src="https://user-images.githubusercontent.com/67285979/218240441-528f007a-e6b4-444b-80b1-69a10149f6b6.png" 
alt="ROS Basics" width="250" border="10"/></p>

* Inside the “basic_comms” package, create a folder named “config”.
* Inside the config folder create a file named “params.yaml” (the file can have any name just make sure follow a convention properly).
* Open the newly created parameter file (params.yaml) and edit it as follows
```
Message: "Parameter YAML File Global“

Group1:  
	Message: "Parameter YAML File local G1"  
	talker:    
		Message: "Parameter YAML File private G1“

Group2:  
	Message: "Parameter YAML File G2"  
	talker:    
		Message: "Parameter YAML File private G2"

```
* Save it and close the file.
* Open the roslaunch file (activity1.launch)
* Modify the launch file as follows, save it and close it.
```
<?xml version="1.0" ?>
<launch>

    <rosparam file = "$(find basic_comms)/config/params.yaml" command = "load" />
    
	<group ns = "Group1">
        <node name="talkerG1" pkg="basic_comms" type="talker.py" output="screen" launch-prefix="gnome-terminal --command" />
        <node name="listenerG1" pkg="basic_comms" type="listener.py" output="screen" launch-prefix="gnome-terminal --command" />
    </group>

    <group ns = "Group2">
        <node name="talkerG2" pkg="basic_comms" type="talker.py" output="screen" launch-prefix="gnome-terminal --command" />
        <node name="listenerG2" pkg="basic_comms" type="listener.py" output="screen" launch-prefix="gnome-terminal --command" />
    </group>

</launch>
```

* Run the modified launch file.
* Open a new terminal and type the following to view the parameters
```
$ rosparam list
```
* To access each parameter inside the "talker.py" script, the get_ parameter function must be modified as follows

Global parameter
```
 hello_str = rospy.get_param(“/Message", "No Parameter Found")  + " " + str(rospy.get_time())
```
Local Parameter
```
 hello_str = rospy.get_param(“Message", "No Parameter Found")  + " " + str(rospy.get_time())
```
Private Parameter
```
 hello_str = rospy.get_param(“~Message", "No Parameter Found")  + " " + str(rospy.get_time())
```

## Activity 4 : Custom Messages
This activity shows the usage of custom messages for the previous Mini Challenge 1.

<p align="center"><img src="https://user-images.githubusercontent.com/67285979/218240617-48e882ee-f746-494b-bf64-62299897c5e4.png" 
alt="ROS Basics" width="350" border="10"/></p>

* In the “basic_comms” package (or the student's own package), create a folder named “msg”
* Inside the folder “msg” create a file called “signal_msg.msg”
* Open the file using a text editor and write the following.
```
 float32 time_x
 float32 signal_y
```
* Save the file. The custom message has been created!

* Open the CMakeLists.txt, of the “basic_comms” package (or the students’ package) and find the following line and modify it as follows
```
find_package(catkin REQUIRED COMPONENTS  rospy  std_msgs  message_generation)

 add_message_files(   
	FILES
   signal_msg.msg 
)

 generate_messages(
   DEPENDENCIES
   std_msgs
 )

 catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES basic_comms
  CATKIN_DEPENDS message_runtime
#  DEPENDS system_lib
)
```

* Save and Close the CmakeLists.txt.
* Open the file package.xml
* Uncomment or add the following lines
```
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend> 
```
* Save and close.

* Open the "signal_generator.py" file.
* Modify it as follows
```
#!/usr/bin/env python
import rospy
import numpy as np
from basic_comms.msg import signal_msg  #Import the message to be used

if _name=='__main_’:

	## Declare the new message to be used
    signal_pub=rospy.Publisher("signal",signal_msg, queue_size=10)    

	rospy.init_node("signal_generator")
    rate = rospy.Rate(10)
    init_time = rospy.get_time()
    msg = signal_msg()

    while not rospy.is_shutdown():
        time = rospy.get_time()-init_time
        signal = np.sin(time)

	    ## Fill the message with the required information	
        msg.time_x = time
        msg.signal_y = signal

	    ## Publish the message
        signal_pub.publish(msg)

        rospy.loginfo("The signal value is: %f at a time %f", signal, time)
        rate.sleep()

   ```

  * Remember to make the nodes executable using the the following command inside the *catkin_ws/src/basic_comms/src* folders 
  ```
    chmod +x foo.py   (change the foo for the script name)
  ```
  * Run the node as previously defined. 