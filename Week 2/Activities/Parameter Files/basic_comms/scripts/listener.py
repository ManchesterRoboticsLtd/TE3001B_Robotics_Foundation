#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("I heard %s", msg.data)

if __name__=='__main__':
    rospy.init_node("listener")
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()