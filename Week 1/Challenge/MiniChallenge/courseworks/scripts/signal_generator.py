#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float32

if __name__=='__main__':

    #Finish configuring your node here (part of the code has already been written as a hint)
    rospy.init_node("signal_generator")
    rate = rospy.Rate(10)
    signal_pub=rospy.Publisher("signal",Float32, queue_size=10)

    while not rospy.is_shutdown():

        #Write your code here

        rate.sleep()