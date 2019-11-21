# -*- coding: utf-8 -*-

__author__ = 'Håvard Brobakken Eig, Olav vikøren Espenes '
__email__ = 'havardei@nmbu.no, olaves@nmbu.no'

import snakes_simulations as cs


def test_winning_numbers():
    s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])
    s.run_simulation(15)
    assert sum(s.winners_per_type().values()) == 15


def test_move():
    a = cs.Player(cs.Board())
    pos1 = a.position
    a.move()
    pos2 = a.position
    assert pos1 != pos2
