from gymnasium.envs.registration import register


register(id="mo-highway-v0", entry_point="mo_gymnasium.envs.highway.highway:MOHighwayEnv")

register(id="mo-highway-fast-v0", entry_point="mo_gymnasium.envs.highway.highway:MOHighwayEnvFast")

register(id="mo-highwaybs-fast-v0", entry_point="mo_gymnasium.envs.highway.highway_bs:MOHighwayEnvFastBS")
