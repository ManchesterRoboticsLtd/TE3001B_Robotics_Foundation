#!/usr/bin/env python
import rospy
from std_msgs.msg import String

if __name__=='__main__':
    pub=rospy.Publisher("chatter",String, queue_size=10)
    rospy.init_node("talker")
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)

        rate.sleep()