# -*- coding: utf-8 -*-


__author__ = 'Håvard Brobakken Eig'
__email__ = 'havardei@nmbu.no'

from walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        if not (left_limit <= start <= right_limit):
            raise ValueError('Start position is out of limit')
        if not (left_limit <= home <= right_limit):
            raise ValueError('Home position is out of limit')
        super().__init__(start, home)
        self.left = left_limit
        self.right = right_limit

    def move(self):
        super().move()
        if self.position < self.left:
            self.position = self.left
        elif self.position > self.right:
            self.position = self.right


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        super().__init__(start, home, seed)
        self.left = left_limit
        self.right = right_limit

    def single_walk(self):

        walker = BoundedWalker(self.start, self.home,
                               self.left, self.right)
        num_steps = 0
        while not walker.is_at_home():
            walker.move()
            num_steps += 1
        return num_steps


if __name__ == '__main__':
    for left_bound in [0, -10, -100, -1000, -10000]:
        steps = BoundedSimulation(0, 20, seed=12345,
                                  left_limit=left_bound,
                                  right_limit=20).run_simulation(20)
        print('Left boundary: {:8d}: {}'.format(left_bound, steps))
