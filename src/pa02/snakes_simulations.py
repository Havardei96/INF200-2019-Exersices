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

    def goal_reached(self):
        pass

    def position_adjustment(self):
        pass
