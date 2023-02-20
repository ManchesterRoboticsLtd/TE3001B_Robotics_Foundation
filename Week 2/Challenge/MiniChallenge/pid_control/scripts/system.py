#!/usr/bin/env python
import rospy
import numpy as np
from pid_control.msg import motor_output
from pid_control.msg import motor_input
from std_msgs.msg import Float32

class SimpleSystem:

  def __init__(self):

    #Set the parameters of the system
    self.sample_time = rospy.get_param("/system_sample_time",0.02)
    self.max_speed = rospy.get_param("/system_max_speed",13.0)
    self.min_input = rospy.get_param("/system_min_input",0.2)
    self.param_K = rospy.get_param("/system_param_K",13.2)
    self.param_T = rospy.get_param("/system_param_T",0.05)
    self.init_conditions = rospy.get_param("/system_initial_cond",0) 

    # Setup Variables to be used
    self.first = True
    self.start_time = 0.0
    self.current_time = 0.0
    self.last_time = 0.0
    self.proc_output = 0.0

    # Declare the input Message
    self.Input = motor_input()
    self.Input.input = 0.0
    self.Input.time = 0.0


    # Declare the  process output message
    self.output = motor_output()
    self.output.output= self.init_conditions
    self.output.time = rospy.get_time()
    self.MotorStatus(self.init_conditions)
  

    # Setup the Subscribers
    rospy.Subscriber("/motor_input",motor_input,self.input_callback)

    #Setup de publishers
    self.state_pub = rospy.Publisher("/motor_output", motor_output, queue_size=1)

  #Define the callback functions
  def input_callback(self,msg):
    self.Input = msg

  #Define the main RUN function
  def run (self):
    #Variable setup
    if self.first == True:
      self.start_time = rospy.get_time() 
      self.last_time = rospy.get_time()
      self.current_time = rospy.get_time()
      self.first = False
  #System
    else:
      #Define sampling time
      self.current_time = rospy.get_time()
      dt = self.current_time - self.last_time
   
      #Dynamical System Simulation
      if dt >= self.sample_time:
        #Dead-Zone
        if(abs(self.Input.input)<=self.min_input):
          self.proc_output+= (-1.0/self.param_T * self.proc_output + self.param_K/self.param_T * 0.0) * dt
        #Saturation
        elif (((-1.0/self.param_T * self.proc_output + self.param_K/self.param_T * self.Input.input)>0.0 and self.proc_output> self.max_speed)or ((-1.0/self.param_T * self.proc_output + self.param_K/self.param_T * self.Input.input)<0.0 and self.proc_output< -self.max_speed)):
          self.proc_output+= (-1.0/self.param_T * self.proc_output + self.param_K/self.param_T * ((1/self.param_K)*self.proc_output)) * dt
        #Dynamic System
        else:
          self.proc_output += dt*((-1.0/self.param_T) * self.proc_output + (self.param_K/self.param_T) * self.Input.input)  
    
        #Message to publish
        self.output.output= self.proc_output
        self.output.time = rospy.get_time() - self.start_time
        self.MotorStatus(self.proc_output)
        #Publish message
        self.state_pub.publish(self.output)

        self.last_time = rospy.get_time()
      
      #else:
      #self.state_pub.publish(self.output)

  # Motor Status Function
  def MotorStatus(self,speed):
    if (abs(speed)<=abs(self.param_K*self.Input.input*0.8) and abs(self.Input.input)<=self.min_input):
      self.output.status = "Motor Not Turning"
    elif (abs(speed)>=self.max_speed):
      self.output.status = "Motor Max Speed"
    else:
      self.output.status = "Motor Turning"



 #Stop Condition
  def stop(self):
  #Setup the stop message (can be the same as the control message)
    print("Stopping")
    self.output.output= 0.0
    self.output.time = rospy.get_time() - self.start_time
    self.output.status = "Motor Not Turning"
    self.state_pub.publish(self.output)
    total_time = rospy.get_time()-self.start_time
    rospy.loginfo("Total Simulation Time = %f" % total_time)



if __name__=='__main__':

 #Initialise and Setup node
 rospy.init_node("Motor_Sim")
 System = SimpleSystem()
 
 # Configure the Node
 loop_rate = rospy.Rate(rospy.get_param("/system_node_rate",100))
 rospy.on_shutdown(System.stop)

 print("The Motor is Running")
 try:
  #Run the node
  while not rospy.is_shutdown(): 
   System.run()
   loop_rate.sleep()
 
 except rospy.ROSInterruptException:
  pass