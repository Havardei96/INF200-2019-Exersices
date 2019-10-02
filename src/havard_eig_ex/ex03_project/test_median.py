# -*- coding: utf-8 -*-

__author__ = 'Håvard Brobakken Eig'
__email__ = 'havardei@nmbu.no'


import pytest


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sorted_data = sorted(data)
    num_elements = len(sorted_data)
    if num_elements % 2 == 1:
        return sorted_data[num_elements // 2]
    elif num_elements == 0:
        raise ValueError
    else:
        return (sorted_data[num_elements // 2 - 1] + sorted_data[
            num_elements // 2]) / 2


def test_median_of_singleton():
    """tests that median funcion works for lists with single items"""
    assert median([4]) == 4


def test_median_odd_number():
    """tests if median function works for lists with length of a odd number"""
    data = [1, 2, 3, 4, 5]
    assert median(data) == 3


def test_median_even_number():
    """tests if median function works for list with a
    length of a even number"""
    data = [1, 2, 3, 4]
    assert median(data) == 2.5


def test_list_with_ordered_elements():
    data = [1, 2, 3]
    assert median(data) == 2


def test_list_with_reverse_ordered_elements():
    data = [3, 2, 1]
    assert median(data) == 2


def test_list_with_unordered_elements():
    data = [1, 3, 2]
    assert median(data) == 2


def test_median_rasis_value_error_on_empty_list():
    """A test checking that requesting the median of an empty list raises a
    ValueError exception"""
    with pytest.raises(ValueError):
        median([])


def test_original_unchanged():
    """A test that ensures that the median function leaves the original
    data unchanged"""
    data = [1, 2, 3]
    median_extracted = median(data)
    assert data == [1, 2, 3] and median_extracted == 2


def test_works_median_with_tuples():
    """A test that ensures that the median function works for tuples as
    well as lists"""
    tuple_data = (1, 2, 3)
    assert median(tuple_data) == 2
