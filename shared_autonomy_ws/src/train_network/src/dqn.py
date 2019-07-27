import rospy
from std_msgs.msg import Int16

import numpy as np 
import math
import random
import time

from collections import deque

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

EPISODES = 10000 #Total Episodes to train the model
T = 500 # Time to complete a Episode

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.init_node('dqn')
        self.action_pub = rospy.Publisher('action_cmd', Int16, queue_size = 1 )
        
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=5000)
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 
        self.epsilon_decay = 
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        # Build a Deep Neural Network
        model = Sequential()
        model.add(Dense(512, input_dim = self.state_size, activation='relu'))
        model.add(Dense(256, input_dim = self.state_size, activation='relu'))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss = 'mse', optimizer=Adam(lr=self.learning_rate))
        return model

    def _remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])  # returns action

    def replay(self, batch_size):
        minibatch = random.sample(self.memory,batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + self.gamma*np.amax(self.model.predict(next_state)[0]);
            else:
                target = reward
            
            target_f = self.model.predict(state)
            


    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)

    def update(self):

    def spin(self):
        rospy.loginfo("DQN agent Initialized")
        rate = rospy.Rate(10)
        rospy.on_shutdown(self.shutdown)
        while not rospy.is_shutdown():
            self.update()
            rate.sleep()
        rospy.spin()

    def is_shutdown(self):
        rospy.loginfo("DQN agent Stopped")
        self.save("dqn_parameters")
        rospy.sleep(1)
        




def main():
    env = EnvironmentGazebo()
    env.init()
    state_size = 1081
    action_size= 5
    agent = DQNAgent(state_size,action_size)
    done = False
    batch_size = 32
    
    for e in range(EPISODES):
        reward_sum = 0
        # preprocess state if required
        state,_,_,_ = env.step(0.0,0.0)

        state = np.reshape(state,[1,state_size])

        for t in range(T):
            action = agent.act(state)
            state, reward, next_state, done = env.step(state, action)
            next_state = np.reshape(next_state, [1,state_size])
            reward_sum = reward_sum + reward
            agent._remember(state, action, reward_sum, next_state, done)
            state = next_state
            if done:
                print("episode: {}/{}, score: {}, e: {:.2}".format(e, EPISODES, reward_sum, agent.epsilon))
                break

        if len(agent.memory) > batch_size:
            agent.replay(batch_size)




if __name__ == '__main__':
    main()