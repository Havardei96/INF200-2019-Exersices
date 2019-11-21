# -*- coding: utf-8 -*-

__author__ = 'Håvard Brobakken Eig, Olav vikøren Espenes '
__email__ = 'havardei@nmbu.no, olaves@nmbu.no'

import random


class Board:
    """
    Defining the board with its snakes, ladders and the goal.
    """
    def __init__(self, *args, **kwargs):
        self.extra = args, kwargs
        self.ladders = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
        self.snakes = {25: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
        self.resilient_move = False
        self.lazy_move = False
        self.goal = 90

    def goal_reached(self, position):
        """
        Returns true if a player has reached or moved beyond the goal.
        """
        if position >= self.goal:
            return True
        return False

    def position_adjustment(self, position):
        """
        Returns the number of positions the player must move forward or
        backward in case of a ladder or a snake.
        """
        if position in self.snakes.keys():
            self.resilient_move = True
            return self.snakes[position] - position
        elif position in self.ladders.keys():
            self.lazy_move = True
            return self.ladders[position] - position
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


class LazyPlayer(Player):

    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.dropped_steps = dropped_steps
        self.climbed_in_last_move = False

    def move(self):
        dropped = self.dropped_steps if self.climbed_in_last_move else 0
        self.position += max(0, random.randint(1, 6) - dropped)
        adjustment = self._board.position_adjustment(self.position)
        self.position += adjustment
        self.climbed_in_last_move = adjustment > 0
        self.num_moves += 1

        
class Simulation:
    def __init__(self, player_field, board=None, seed=1234567,
                 randomize_players=False):
        self._player_field = player_field
        self._player_types = frozenset(pc.__name__ for pc in player_field)
        self._board = board if board is not None else Board()
        self._results = []
        self._randomize = randomize_players
        random.seed(seed)

    def single_game(self):
        players = [player(self._board) for player in self._player_field]
        if self._randomize:
            random.shuffle(players)

        while True:
            for player in players:
                player.move()
                if self._board.goal_reached(player.position):
                    return player.num_moves, type(player).__name__

    def run_simulation(self, num_games):
        for _ in range(num_games):
            self._results.append(self.single_game())

    def get_results(self):
        return self._results

    def players_per_type(self):
        return {player_type.__name__:
                self._player_field.count(player_type)
                for player_type in frozenset(self._player_field)}

    def winners_per_type(self):
        winner_types = list(zip(*self._results))[1]
        return {player_type: winner_types.count(player_type)
                for player_type in self._player_types}

    def durations_per_type(self):
        return {player_type: [d for d, t in self._results if t == player_type]
                for player_type in self._player_types}


if __name__ == "__main__":
    testsim = Simulation(
        [Player, ResilientPlayer, LazyPlayer, ResilientPlayer], seed=69
    )
    testsim.run_simulation(10)
    print(testsim.get_results())
    print(testsim.winners_per_type())
    print(testsim.durations_per_type())
    print(testsim.players_per_type())
