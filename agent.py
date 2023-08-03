import pygame 
import random
import torch
import numpy as np
from collections import deque
from main import Tiles, Game

MAXMEM = 100000
BATCH_SIZE = 1000
LR = 0.01

class Agent:

    def __init__(self):
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0
        self.memory = deque(maxlen = MAXMEM)
        self.model = None
        self.trainer = None
        

    def get_state(self,game):
        return np.array(game.get_board_state())

    def remember(self, state, action, reward, next_state, done):
        self.memory.append(state,action, reward, next_state, done)


    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE) #list of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)
        

    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state,action, reward, next_state, done)

    def get_action(self,state):
        self.epsilon = 80 - self.n_games
        final_move = 0
        if random.randint(0, 200) < self.epsilon:
            final_move = random.choice([1,2,3,4])
        else:
            state0 = torch.tensor(state)
            prediction = self.model.predict(state0)
            final_move = torch.argmax(prediction).item()
            
        return final_move

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0 
    agent = Agent()
    game = Game()
    while True:
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)
        reward, done, score = game.step(final_move)
        state_new = agent.get_state(game)
        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()

            print("Game", agent.n_games, "Score", score,"Record", record)



if __name__ == "__main__":
    train()