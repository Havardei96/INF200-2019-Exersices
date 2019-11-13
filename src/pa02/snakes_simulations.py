# -*- coding: utf-8 -*-

__author__ = 'Håvard Brobakken Eig, Olav vikøren Espenes '
__email__ = 'havardei@nmbu.no, olaves@nmbu.no'


class Board:
    ladders = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
    snakes = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
    winning_position = 90
    def __init__(self, ladders=None, snakes=None, winning_position=None):
        if ladders is None:
            ladders = Board.ladders
        if snakes is None:
            snakes = Board.snakes
        if winning_position is None:
            winning_position = Board.winning_position
        for start, destination in ladders:
            if destination <= start:
                raise ValueError('wrong ladders value')
        for start, destination in snakes:
            if destination >= start:
                raise ValueError('wrong snake value')
        self.snakes_and_ladders = {start: end
                                   for start, end in snakes + ladders}
        self.winning_position = Board.winning_position if goal is None
            else goal

        if self.winning_position <= 0
            raise ValueError('Wrong goal value. Input must be above'
                             'start position')

    def goal_reached(self, position):
        return position >= winning_position

    def position_adjustment(self, position):
        if position in snakes:
            num_moves = snakes[position]-position
            return num_moves
        elif position in ladder:
            num_moves = ladder[position]-position
            return num_moves
        else
            return 0

class Player:

    def __init__(self, board):
        self.board = board
        self.position = 0
        self.num_of_moves = 0


