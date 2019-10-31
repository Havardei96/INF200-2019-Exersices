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
        self.current = (a * self.seed) % m
        self.seed = self.current
        return self.current


class ListRand:
    def __init__(self, numbers):
        self.numbers = numbers
        self.count_list = 0

    def rand(self):
        self.count_list += 1
        if self.count_list > len(self.numbers):
            raise RuntimeError('End of list error')
        else:
            return self.numbers[self.count_list-1]


if __name__ == "__main__":
    list_test = ListRand([1, 3, 5, 6])
    LCG = LCGRand(6)
    for _ in range(4):
        print(list_test.rand())
        print(LCG.rand())
