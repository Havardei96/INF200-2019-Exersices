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
        self.position += 2 * random.randint(0, 1) - 1
        self.moves += 1

    def is_at_home(self):
        return self.position == self.home

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.moves


class Simulation:

    def __init__(self, start, home, seed):
        self.start = start
        self.home = home
        random.seed(seed)

    def single_walk(self):
        walker = Walker(self.start, self.home)
        while not walker.is_at_home():
            walker.move()
        return walker.get_steps()

    def run_simulation(self, num_walks):
        return [self.single_walk() for _ in range(num_walks)]


if __name__ == '__main__':
    print(Simulation(0, 10, 12345).run_simulation(20))
    print(Simulation(0, 10, 12345).run_simulation(20))
    print(Simulation(0, 10, 54321).run_simulation(20))

    print(Simulation(10, 0, 12345).run_simulation(20))
    print(Simulation(10, 0, 12345).run_simulation(20))
    print(Simulation(10, 0, 54321).run_simulation(20))
