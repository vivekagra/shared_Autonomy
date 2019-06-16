import numpy as np
import random
import rospy
import roslib
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
from std_msgs.msg import Int16

episodes = 1000

class shared_aut():
    def __init__(self,state_size,action_size):
        rospy.init_node('autonomy')
        rospy.Publisher('cmd_action', Int16, queue_size=10)
        rospy.Subscriber()
        self.action_size = action_size
        self.state_size = state_size
        self.gamma = 0.95
        self.epsilon = 1.0
        self.max_epsilon = 1.0
        self.min_epsilon = 0.01
        self.model = self.build_model
        self.learning_rate = 0.001
        
    def build_model(self):
        model = Sequential()
        model.add(Desnse(512, input_dim = self.state_size, activation = 'relu'))
        model.add(Desnse(256, input_dim = self.state_size, activation = 'relu'))
        model.add(Desnse(128, activation = 'relu'))
        model.add(Dense(self.action_size, activation = 'linear'))
        model.compile(loss='mse', optimizer = Adam(lr=self.learning_rate))
        return model
    
    def action(self,state):
        #exploration
        if(epsilon<=np.random.rand()):
            return random.randrange(self.action_size)
        #exploitation
        else:
            act = self.model.predict(state)
            
        
if __name__ == '__main__':
    # define initial variables
    state_size  = 1024
    action_size = 6
    batch_size  = 32
    autonomy = shared_aut(state_size,action_size)
    done = False
    
    for e in range(episodes):
        rewrd_sum = 0;
        
        """ ++++++++------ set the environment and take current state from environment --------++++++++"""
        
        # resize state
        state = np.reshape(state,[1,state_size])
        
        