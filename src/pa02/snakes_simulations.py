# -*- coding: utf-8 -*-

__author__ = 'Håvard Brobakken Eig, Olav vikøren Espenes '
__email__ = 'havardei@nmbu.no, olaves@nmbu.no'

import random


class Board:
    ladders = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
    snakes = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
    winning_position = 90

    def __init__(self, ladders=None, snakes=None, winning_position=None):
        if ladders is None:
            seclf.ladders = Board.ladders
        if snakes is None:
            self.snakes = Board.snakes
        for start, destination in self.ladders:
            if destination <= start:
                raise ValueError('wrong ladders value')
        for start, destination in self.snakes:
            if destination >= start:
                raise ValueError('wrong snake value')
        self.snakes_and_ladders = {start: end
                                   for start, end in snakes + ladders}
        self.winning_position = Board.winning_position if self.winning_position is None else winning_position

        if self.winning_position <= 0:
            raise ValueError('Wrong goal value. Input must be above'
                             'start position')

    def goal_reached(self, position):
        return position >= self.winning_position

    def position_adjustment(self, position):
        if position in self.snakes:
            num_moves = self.snakes[position]-position
            return num_moves
        elif position in self.ladders:
            num_moves = self.ladders[position]-position
            return num_moves
        else:
            return 0


class Player:

    def __init__(self, board):
        self._board = board
        self.position = 0
        self.num_moves = 0

    def move(self):
        self.position += random.randint(1, 6)
        self.position += self._board.position_adjustment(self.position)
        self.num_moves += 1


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.extra_steps = extra_steps
        self.went_down_in_last_move = False

    def move(self):
        extra = self.extra_steps if self.went_down_in_last_move else 0
        self.position += random.randint(1, 6) + extra
        adjustment = self._board.position_adjustment(self.position)
        self.position += adjustment
        self.went_down_in_last_move = adjustment < 0
        self.num_moves += 1



