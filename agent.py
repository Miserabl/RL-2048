import pygame
import gymnasium as gym
import numpy as np
from train import gameEnv
from stable_baselines3 import DQN
import time


model = DQN.load("C:\\Users\\misra\\RL-2048\\RL-2048\\trained_agent")

env = gameEnv()
obs, _ = env.reset()



  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()        
    action, _ = model.predict(obs)
    obs, reward, done, _, _ = env.step(action)
    env.render()

    if done:
        print("Game Over!")
        print("Max Score: ", np.max(obs))
        break

    time.sleep(0.01)  
time.sleep(5)