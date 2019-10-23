# -*- coding: utf-8 -*-

__author__ = 'Håvard Brobakken Eig'
__email__ = 'havardei@nmbu.no'

import random


class Walker:
    def __init__(self, start, home):
        self.position = start
        self.home = home
        self.moves = 0

    def move(self):
        self.moves += 1
        if random.randint(0, 1) == 1:
            self.position += 1
        else:
            self.position -= 1

    def is_at_home(self):
        if self.position == self.home:
            return True
        else:
            return False

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.moves

    def walking_start_home(self):
        while not self.is_at_home():
            self.move()
        return self.moves
