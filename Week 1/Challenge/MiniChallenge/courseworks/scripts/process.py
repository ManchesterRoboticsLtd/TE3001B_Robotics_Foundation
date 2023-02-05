#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float32

#Global variable to store the data from the message in the /signal topic
signal_data = 0

# Example Callback Function (Hint)
def callback(msg):
    global signal_data
    signal_data = msg.data


if __name__=='__main__':
    
    #Finish configuring your node here (part of the code has already been written as a hint)
    rospy.init_node("process")
    #Subscriber example (Hint)
    rospy.Subscriber("/signal", Float32, callback)
    rate = rospy.Rate(10)


    while not rospy.is_shutdown():

        #Write your code here

        rate.sleep()