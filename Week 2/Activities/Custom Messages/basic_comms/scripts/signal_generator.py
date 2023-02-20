#!/usr/bin/env python
import rospy
import numpy as np
from basic_comms.msg import signal_msg

Amplitude = rospy.get_param("signalGen_Amplitude",1.0)
Omega = rospy.get_param("signalGen_freq",1.0)
msg = signal_msg()
msg.time_x = 0.0
msg.signal_y = 0.0

if __name__=='__main__':
    signal_pub=rospy.Publisher("signal",signal_msg, queue_size=10)
    rospy.init_node("signal_generator")
    rate = rospy.Rate(10)
    init_time = rospy.get_time()


    while not rospy.is_shutdown():
        time = rospy.get_time()-init_time
        signal = Amplitude*np.sin(Omega*time)
        
        msg.time_x = time
        msg.signal_y = signal
        signal_pub.publish(msg)
        rospy.loginfo("The generated signal value is: %f at a time %f", signal, time)

        rate.sleep()