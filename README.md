# RL-2048
A pygame implementation of 2048 and training a reinforcement learning model to play it

Requirements:
Install pygame, OpenAi Gym, numpy libraries
~~ pip install pygame
~~ pip install gym
~~ pip install numpy


There are 3 major files: 
The 2048_game.py which is my version of the game 2048 created in pygame meant to be played by a user

The train.py file has the modified version of the 2048 file in which its ready to be used by Reinforcement Learning agent,  as well as the additional functions required for the agent to learn

Note: After train.py is ran, it will create a file called trained_agent.zip that is then loaded/tested in the agent.py file

The agent.py file is for the testing of the agent, to render its "learned" gameplay in real time and print the score it gets.
