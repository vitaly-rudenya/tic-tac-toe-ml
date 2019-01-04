import random

import numpy as np

__author__ = "Vitaly Rudenya"

from .game import Game
from .gamelayer import Layer


class TicTacToe(Game):

    def __init__(self):
        self.forbidden_moves = []
        self.field = []
        self.game_layers = []

        self.reset()
        self.state_changed = True
        self.steps = 0
        self.score = 0

    @property
    def name(self):
        return "Snake"

    @property
    def nb_actions(self):
        return 9

    def play(self, action):
        assert action in range(9), "Invalid action."
        self.move_snake(action)

    def move_snake(self, action):
        self.steps = self.steps - 1
        if action in self.forbidden_moves:
            #self.score += 0.01
            self.forbidden_moves.remove(action)
            self.field[action // 3][action % 3] = 1

            if len(self.forbidden_moves) > 0 and not self.is_won():
                player_action = random.sample(self.forbidden_moves, 1)[0]
                self.field[player_action // 3][player_action % 3] = -1
                self.forbidden_moves.remove(player_action)
        #else:
            #self.score -= 0.01

    def get_state(self):
        return np.asarray(self.field)

    def get_score(self):
        if self.is_won():
            score = 0.8
        elif self.is_player_lose():
            score = -0.8
        else:
            score = 0
        return score + self.score

    def reset(self):
        self.score = 0
        self.forbidden_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.steps = 9
        self.field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.game_layers = [Layer(self.field, 0, 1, 2, 0, 0, 0),
                            Layer(self.field, 0, 1, 2, 1, 1, 1),
                            Layer(self.field, 0, 1, 2, 2, 2, 2),

                            Layer(self.field, 0, 0, 0, 0, 1, 2),
                            Layer(self.field, 1, 1, 1, 0, 1, 2),
                            Layer(self.field, 2, 2, 2, 0, 1, 2),

                            Layer(self.field, 0, 1, 2, 0, 1, 2),
                            Layer(self.field, 2, 1, 0, 0, 1, 2)]

    def is_over(self):
        return len(self.forbidden_moves) == 0 or self.is_won() or self.is_player_lose() or self.steps <= 0

    def is_won(self):
        won = False
        for game_layer in self.game_layers:
            won = won or game_layer.is_player_won()

        return won

    def get_possible_actions(self):
        return self.forbidden_moves

    def is_player_lose(self):
        won = False
        for game_layer in self.game_layers:
            won = won or game_layer.is_player_loose()

        return won
