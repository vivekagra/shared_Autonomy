import numpy as np 
import random
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.parameter as Parameter
from torch.autograd import Variable
import torch.optim as optim
import torch.multiprocessing as mp
import gym
import os


# define some default paramenters
gamma = 0.9
learning_rate = 
MAX_EP = 4000


# use the id of environment you wanat to use
env = gym.make('')
N_S = gym.observation_space.shape[0]
N_A = gym.action_space.shape[0]

class ActorCritic(nn.Module):
	def __init__(self, state_dim, action_dim):
		super(ActorCritic, self).__init__()
		self.state_dim = state_dim
		self.action_dim = action_dim
		
 