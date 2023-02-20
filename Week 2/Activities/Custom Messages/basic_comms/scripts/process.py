#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float32
from basic_comms.msg import signal_msg

angle = rospy.get_param("process_angle",np.pi/2.0)
offset = rospy.get_param("process_offset",1.0)
amplitude = rospy.get_param("process_amplitude",0.5)

signal_data = 0.0
time_data = 0.0


def callback(msg):
    global signal_data, time_data
    signal_data = msg.signal_y/rospy.get_param("signalGen_Amplitude",1.0)
    time_data = msg.time_x * rospy.get_param("signalGen_freq",1.0)


# Wrap to Pi function
def wrap_to_Pi(theta):
    result = np.fmod((theta+np.pi),(2*np.pi))
    if (result<0):
        result += 2 * np.pi
    return result - np.pi


if __name__=='__main__':
    rospy.init_node("process")
    rospy.Subscriber(rospy.get_namespace()+"signal", signal_msg, callback)
    pub=rospy.Publisher("proc_signal",Float32, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        if (wrap_to_Pi(time_data) >= -np.pi/2 and wrap_to_Pi(time_data)<= np.pi/2):
            signal = signal_data * np.cos(angle) + np.sqrt(1-np.power((signal_data),2)) * np.sin(angle) 
        else:
            signal = signal_data * np.cos(angle) - np.sqrt(1-np.power((signal_data),2)) * np.sin(angle)

        processed_signal =  (amplitude * signal) + offset
        rospy.loginfo("The proessed signal value is: %f at a time %f", processed_signal, time_data)
        
        pub.publish(processed_signal)
        rate.sleep()