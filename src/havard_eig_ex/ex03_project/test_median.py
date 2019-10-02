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
    data = [1, 2, 3, 4, 5]
    assert median(data) == 3


def test_median_even_number():
    data = [1, 2, 3, 4]
    assert median(data) == 2.5


def test_list_with_ordered_elements():
    pass


def test_list_with_reverse_ordered_elements():
    pass


def test_list_with_unordered_elements():
    pass


def test_median_rasis_value_error_on_empty_list():
    """A test checking that requesting the median of an empty list raises a
    ValueError exception"""
    with pytest.raises(ValueError):
        median([])


def test_original_unchanged():
    """A test that ensures that the median function leaves the original
    data unchanged"""
    pass


def test_works_median_with_tuples():
    """A test that ensures that the median function works for tuples as
    well as lists"""
    pass
