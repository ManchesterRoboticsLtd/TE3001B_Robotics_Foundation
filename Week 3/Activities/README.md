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

# Week 3: Activities and Examples

In this folder, the student will find the files containing the solution for Activity 1.
### << We Encourage the students to NOT USE the files and follow the instructions during class and in the presentation to make this activity !! >>

### Requirements
* Ubuntu in VM or dual booting
* ROS installed
* Arduino IDE
* Arduino IDE configured
  * Follow the tutorial on how to install it in presentation:
       *MCR2_ROS_ArduinoIDE_Configuration*
* Arduino ROS Libraries
* Hackerboard/Arduino Mega/Arduino Uno

## Instructions

* Configure the Arduino IDE according to the presentation "*MCR2_ROS_ArduinoIDE_Configuration*"
* Install the ROS Arduino libraries 
    * Open the folder "*ROS_Arduino_Library*"
    * Open the folder according to your OS.
    * Download the .zip file. 
    * Import the libraries according to the tutorial in the following link
        [Arduino IDE Libraires](https://docs.arduino.cc/software/ide-v1/tutorials/installing-libraries)
* Compile the projects
* Upload it to the Hackerboard or Arduino

## Activity 1 : Rosserial
* In this activity, a node running a simple publisher will be made.
* This node will run inside the microcontroller and will communicate with the computer through serial communication using the rosserial protocol.
* The node will publish a simple string message “Hello World”, which will be read by the computer using a ros command line for simplicity.
* This activity will be divided into two parts. The first part involving Arduino IDE for programming the MCU. 
* The second part involving the commands required to connect to the MCU to the computer.

1. Open Arduino IDE (previously configured).
2. Type the following code
```
#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle  nh;

std_msgs::String str_msg;
ros::Publisher chatter("chatter", &str_msg);

char hello[13] = "hello world!";

void setup()
{
  nh.initNode();
  nh.advertise(chatter);
}

void loop()
{
  str_msg.data = hello;
  chatter.publish( &str_msg );
  nh.spinOnce();
  delay(1000);
}
```

3. Select the board to be used 
   * Tools>Board For Arduino Select Arduino AVR Boards>Arduino Mega or Mega 2560

    * For Hackerboard select ESP32 Arduino > DOIT ESP32 DEVKIT V1

4. Connect the board
5. Select the port to be used Tools>Port
    * If working on the VM, you must first select the option Connect to a virtual machine when automatically prompted (shown) and then select the port.

6.  Select the board to be used Tools>Board
    * For Arduino Select Arduino AVR Boards>Arduino Mega or Mega 2560
    * For Hackerboard select ESP32 Arduino > DOIT ESP32 DEVKIT V1
7. Upload your code

9. Connect the board to the computer with ROS.
10. (In Ubuntu) Make sure the port permissions are granted for the user. 

    * In a new terminal type cd /dev to visualise the port designated by Ubuntu to the MCU. This port are usually called /ttyACM0 or /ttyUSB0.
```
 sudo chmod 666 /dev/ttyACM*
 sudo chmod 666 /dev/ttyUSB*
```
 
11. Launch the roscore on a new terminal
```
roscore
```
12. In a new terminal use the command line tool rosrun and select the port type (USB or ACM).

```
 rosrun rosserial_python serial_node.py /dev/ttyUSB0 
```

13. In a new terminal subscribe to the topic using the command 
```
rostopic echo chatter 
```
