# -*- coding: utf-8 -*-

__author__ = 'Håvard Brobakken Eig'
__email__ = 'havardei@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.current = 0

    def rand(self):
        a = 7**5
        m = 2**31-1
        self.current = (a * self.current) % m
        self.seed = self.current
        return self.current


class ListRand:
    def __init__(self, numbers):
        self.numbers = numbers
        self.calls = 0

    def rand(self):
        self.calls += 1
        if self.calls < len(self.numbers):
            raise RuntimeError('End of list error')
        else:
            return self.numbers(self.calls-1)
