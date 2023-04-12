import gymnasium.spaces as spaces
import numpy as np
from gymnasium.spaces import Box
from gymnasium.spaces.utils import flatten_space, flatten
import gymnasium
import mo_gymnasium as mo_gym
from gymnasium import spaces
from gymnasium.wrappers import FlattenObservation

box = Box(0.0, 1.0, shape=(3, 4, 5))
print(box)
box = flatten_space(box)
# print(box)box = Box(0.0, 1.0, shape=(3, 4, 5))
print(box)

# box = Box(-inf, inf, (5, 5), float32)
box = Box(-np.inf, np.inf, (5, 5))
print(box)
box = flatten_space(box)
print(box)

env = mo_gym.make("mo-highway-fast-v0")
wrapped_env = FlattenObservation(env)
obs, info = env.reset()
print(obs)#info
print('wrap env observation')
print(wrapped_env.observation_space)
wrapped_obs, wrapped_obs_info = wrapped_env.reset()
print(wrapped_obs)#, wrapped_obs_info

'''
box = Box(0.0, 1.0, shape=(3, 4, 5))
# print(box)
box = flatten_space(box)
# print(box)

vehicles_count = 5
len_features = 5
highway_space = spaces.Box(shape=(vehicles_count, len_features), low=-np.inf, high=np.inf, dtype=np.float32)

# print(highway_space)
highway_space = flatten_space(highway_space)
# print(highway_space)

vehicles_count = 5
len_features = 5
highway_space = Box(shape=(vehicles_count, len_features), low=-np.inf, high=np.inf, dtype=np.float32)

# print(highway_space)
highway_space = flatten_space(highway_space)
# print(highway_space)

# print(flatten(highway_space, highway_space.sample()))

# print(gymnasium.__version__)

'''