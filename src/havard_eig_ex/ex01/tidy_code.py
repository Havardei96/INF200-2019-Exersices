__author__ = 'havard eig'
__email__ = 'havardei@nmbu.no'


from random import randint


def your_guess():
    input_guess = 0
    while input_guess < 1:
        input_guess = int(input('Your guess: '))
    return input_guess


def two_dices_throw():
    return randint(1, 6) + randint(1, 6)


""" two dices thrown and added together
"""


def guess_qual_throw(throww, guesss):
    """checks if sum of dices equals your guess
    """
    return throww == guesss


if __name__ == '__main__':
    false_check = False
    attempts = 3
    throw = two_dices_throw()
    while not false_check and attempts > 0:
        guess = your_guess()
        false_check = guess_qual_throw(throw, guess)
        if not false_check:
            print('Wrong, try again!')
            attempts -= 1
    if attempts > 0:
        print('You won {} points.'.format(attempts))
    else:
        print('You lost. Correct answer: {}.'.format(throw))
