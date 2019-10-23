

__author__ = 'Håvard Brobakken Eig, Olav Vikøren Espenes'
__email__ = 'havardei@nmbu.no, olaves@nmbu.no'


import random
import numpy as np


def single_game(num_players1):
    fixed_position = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
                      24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
    position = [0] * num_players1
    while_playing = True
    moves = 0
    while while_playing:
        for player in range(num_players1):
            position[player] += random.randint(1, 6)
            if position[player] in fixed_position:
                position[player] = fixed_position[position[player]]
        if max(position) >= 90:
            while_playing = False
        moves += 1
    return moves


def multiple_games(num_games2, num_players2):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games2 : int
        Number of games to play
    num_players2 : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """
    list_games = []
    for games in range(num_games2):
        list_games.append(single_game(num_players2))
    return list_games


def multi_game_experiment(num_games3, num_players3, seed1):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games3 : int
        Number of games to play
    num_players3 : int
        Number of players in the game
    seed1 : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the number of moves needed in each game.
    """
    random.seed(seed1)

    return multiple_games(num_games3, num_players3)


if __name__ == '__main__':
    seed = 12345
    num_players = 4
    num_games = 100
    list_of_won_games = multi_game_experiment(num_games, num_players, seed)
    print('The shortest game took {0} throws to finish and the longest game'
          ' {1} throws'.format(min(list_of_won_games), max(list_of_won_games)))
    print('Median game duration is {0} throws'
          .format(np.median(list_of_won_games)))
    print('Mean game duration is {0} with a standard deviation of {1}'
          .format(np.mean(list_of_won_games), np.std(list_of_won_games)))
