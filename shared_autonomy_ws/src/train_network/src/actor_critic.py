import numpy as np 
import random
import gym
import os
from tensorboard import summary

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.parameter as Parameter
from torch.autograd import Variable
import torch.optim as optim
import torch.multiprocessing as mp



# define some default paramenters
ENV_ID = "Puzzle-v1"
GAMMA = 0.9
LEARNING_RATE = 0.001
MAX_EP = 4000
BATCH_SIZE = 32
TEST_ITERS = 10000

# use the id of environment you wanat to use
env = gym.make('')
N_S = gym.observation_space.shape[0]
N_A = gym.action_space.shape[0]

class ActorCritic(nn.Module):
	def __init__(self, state_dim, action_dim):
		super(ActorCritic, self).__init__()
		self.state_dim = state_dim
		self.action_dim = action_dim
		
 