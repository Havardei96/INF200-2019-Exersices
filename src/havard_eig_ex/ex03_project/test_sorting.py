# -*- coding: utf-8 -*-

__author__ = 'Håvard Brobakken Eig'
__email__ = 'havardei@nmbu.no'


def bubble_sort(dataa):
    data_list = list(dataa)
    for i in range(len(data_list) - 1, 0, -1):
        for j in range(i):
            if data_list[j] > data_list[j + 1]:
                replace_temp = data_list[j]
                data_list[j] = data_list[j + 1]
                data_list[j + 1] = replace_temp
    return data_list


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    assert bubble_sort([3, 2, 1]) != [3, 2, 1]


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data != data


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [3, 2, 1]
    sorted = bubble_sort(data)
    sort_sorted = bubble_sort(sorted)
    assert sort_sorted == sorted


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    data = [3, 2, 1]
    assert bubble_sort(data) == sorted(data)


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    data = [1, 1, 1, 1]
    sorted_data = bubble_sort(data)
    assert data == sorted_data


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    pass
