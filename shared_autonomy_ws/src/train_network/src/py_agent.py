import rospy
import numpy as np 
from geometry_msgs.msg import Twist

# this class contains an agent that communicates with turtlebot in real world as well as gazebo environment 
# this function sends environment information to the other training agents, information include image frames, obstacle distance, target distance, etc.
# receives action to be performed on robot and send action to 
# sends reward of taking action
class Gazeboenvironment:

    def __init__():
        rospy.init_node('pyagent')
        input_pub = rospy.Publisher