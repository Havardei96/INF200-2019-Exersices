

__author__ = 'Håvard Brobakken Eig, Olav Vikøren Espenes'
__email__ = 'havardei@nmbu.no, olavzzz@bbc.bbc'


import random


def snakes_ladder(position):
    landed_position = [1, 8, 36, 43, 49, 65, 68, 24, 33, 42, 56, 64, 74, 87]
    new_position = [40, 10, 52, 62, 79, 82, 85, 5, 3, 30, 37, 27, 12, 70]
    if position in landed_position:
        return new_position[landed_position.index(position)]
    else:
        return position


def play_one_player():
    position = 0
    moves = 0
    while position <= 90:
        position = position + random.randint(1, 6)
        position = snakes_ladder(position)
        moves += 1
    return moves


def single_game(num_players):
    list_plays = []
    for player in range(num_players):
        test = play_one_player()
        list_plays.append(test)
    winning_moves = min(list_plays)
    return winning_moves

def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """
    pass

def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """
    pass