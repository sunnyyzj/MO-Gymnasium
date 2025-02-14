import numpy as np
from gymnasium.spaces import Box
from gymnasium.utils import EzPickle
from highway_env.envs import HighwayEnv, HighwayEnvFast, HighwayEnvBS


class MOHighwayEnv(HighwayEnv, EzPickle):
    """
    ## Description
    Multi-objective version of the HighwayEnv environment.

    See [highway-env](https://github.com/eleurent/highway-env) for more information.

    ## Reward Space
    The reward is 3-dimensional:
    - 0: high speed reward
    - 1: right lane reward
    - 2: collision reward
    """

    def __init__(self, *args, **kwargs):
        EzPickle.__init__(self, *args, **kwargs)

        super().__init__(*args, **kwargs)
        self.reward_space = Box(low=np.array([0.0, 0.0, -1.0]), high=np.array([1.0, 1.0, 0.0]), shape=(3,), dtype=np.float32)
        self.reward_dim = 3

    def step(self, action):
        obs, reward, terminated, truncated, info = super().step(action)
        rewards = info["rewards"]
        vec_reward = np.array(
            [
                rewards["high_speed_reward"],
                rewards["right_lane_reward"],
                -rewards["collision_reward"],
            ],
            dtype=np.float32,
        )
        vec_reward *= rewards["on_road_reward"]
        info["original_reward"] = reward
        return obs, vec_reward, terminated, truncated, info


class MOHighwayEnvFast(HighwayEnvFast):
    """A multi-objective version of the HighwayFastEnv environment."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reward_space = Box(low=np.array([0.0, 0.0, -1.0]), high=np.array([1.0, 1.0, 0.0]), shape=(3,), dtype=np.float32)
        self.reward_dim = 3

    def step(self, action):
        obs, reward, terminated, truncated, info = super().step(action)
        rewards = info["rewards"]
        vec_reward = np.array(
            [
                rewards["high_speed_reward"],
                rewards["right_lane_reward"],
                -rewards["collision_reward"],
            ],
            dtype=np.float32,
        )
        vec_reward *= rewards["on_road_reward"]
        info["original_reward"] = reward
        return obs, vec_reward, terminated, truncated, info

class MOHighwayEnvFastBS(HighwayEnvBS):
    """A multi-objective version of the HighwayFastEnv environment."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reward_space = Box(low=-2.0, high=4.0, shape=(2,), dtype=np.float32)
        # self.observation_space = _convert_space(self.observation_space)
        # self.action_space = _convert_space(self.action_space)

    def reset(self, seed=None, **kwargs):
        obs, info = super().reset(seed=seed, **kwargs)
        # self.observation_space = _convert_space(self.observation_space)
        # self.action_space = _convert_space(self.action_space)
        return obs, info

    def step(self, action):
        obs, reward, terminated, truncated, info = super().step(action)
        rewards = info["rewards"]
        vec_reward = np.array(
            [
                rewards["tran_reward"],
                rewards["tele_reward"]
            ],
            dtype=np.float32,
        )
        info["original_reward"] = reward
        return obs, vec_reward, terminated, truncated, info