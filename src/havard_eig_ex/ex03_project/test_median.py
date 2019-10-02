# -*- coding: utf-8 -*-

__author__ = 'Håvard Brobakken Eig'
__email__ = 'havardei@nmbu.no'


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
        else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


def test_median_of_singleton():
    """tests that median funcion works for lists with single items"""
    assert median([4]) == 4


def test_median_odd_number():
    """tests if median function works for lists with length of a odd number"""
    data = [1, 2, 3, 4, 5]
    assert median(data) == 3
