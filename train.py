import gymnasium as gym
import numpy as np
from game_training_class import Game
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv
import time
import pygame
import os

class gameEnv(gym.Env):
    def __init__(self):
        self.game = Game()
        self.action_space = gym.spaces.discrete.Discrete(4)
        self.observation_space = gym.spaces.Box(low = 0, high = 2048, shape = (4,4), dtype = np.int16)
        self.prev_score = None
        self.prev_len = None

    def reset(self, **kwargs):
        self.game.reset()
        self.prev_score = None
        self.prev_len = None
        return np.reshape(self.game.get_board_state(), (4,4)), None
    
    def step(self, action):
        self.game.step(action)
        curr_len = len([i for i in self.game.get_board_state() if i != 0])
        if self.prev_score is not None and self.prev_score == self.game.score and self.prev_len is not None and self.prev_len == curr_len:
            penalty = 50
        else:
            self.prev_score = self.game.score
            self.prev_len = curr_len
            penalty = 0
        
        reward = self.game.score - penalty
        done = self.game.lose()
        observation = np.reshape(self.game.get_board_state(), (4,4))
        return observation, reward, done, False, {}
    
    def render(self, mode = "human"):
        self.game.wait()
        
   
        
if __name__ == "__main__":
    env = gameEnv()
    env = DummyVecEnv([lambda: env])
    model = DQN("MlpPolicy", env, learning_rate= 0.01, verbose = 1)
    model.learn(100000)

    if os.path.exists("RL-2048\\trained_agent"):
        os.remove("RL-2048\\trained_agent")

    model.save("RL-2048\\trained_agent")








