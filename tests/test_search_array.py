import pytest
import numpy as np

from mds_array_manipulation.search_array import search_array

# The following tests are for the function search_array

#Test with 1D array
def test_1d_search(one_d_int_array):
    ind = search_array(one_d_int_array, 3)
    assert ind == 2
    
#Test with 1D array with multiple matching elements, to ensure it only returns the first match
def test_1d_search_multiple_match(one_d_int_array):
    ind = search_array(one_d_int_array, 1)
    assert ind == 0

#Test with 2D array
def test_2d_array(two_d_int_array):
    with pytest.raises(ValueError):
        search_array(two_d_int_array, 10)


#Test with element not in array
def test_1d_array_no_match(one_d_int_array):
    ind = search_array(one_d_int_array, 1000)
    assert ind == -1

#Test empty array
def test_1d_array_no_match(empty_array):
    ind = search_array(empty_array, 1)
    assert ind == -1

#Test numeric type
def test_1d_float_array(one_d_float_array):
    ind = search_array(one_d_float_array, 3.14)
    assert ind == 2

#Test string type
def test_1d_string_array(one_d_string_array):
    ind = search_array(one_d_string_array, 'frog')
    assert ind == 4

#Test case sensitive search
def test_1d_string_array(one_d_string_array):
    ind = search_array(one_d_string_array, 'Frog')
    assert ind == -1

#Test tuple
def test_tuple_array():
    tuple_array = np.array([(1,2), (3,4), (5,6)], dtype="i, i")
    with pytest.raises(TypeError):
        search_array(tuple_array, (3,4))

# checks if the function correctly handles inputs that are not numpy arrays
def test_input_not_numpy_array():
    non_numpy_inputs = [
        [1, 2, 3],
        (1, 2, 3),
        100,
        "not a numpy array",
    ]
    for input in non_numpy_inputs:
        with pytest.raises(TypeError):
            search_array(input, 20)

# Test non 1D array
def test_non_1d_array(two_d_int_array):
    with pytest.raises(ValueError):
        search_array(two_d_int_array, 20)
