def binary_search(array, search):
    ''' 05.5: Return TRUE if search exists in array. '''

    # Initialize the bounding indices.
    i_first = 0
    i_last = len(array) - 1

    assert type(array) == list
    assert len(array) >= 0
    if __debug__:
        for element in array:
            assert type(element == type(search))

    # Continue as long as there are elements in the range.
    while i_first <= i_last:
        i_middle = (i_first + i_last) // 2
        
        assert i_first <= i_last
        assert 0 <= i_middle < len(array)

        # Too high or too low.
        assert type(i_middle) == int
        if array[i_middle] < search:
            i_first = i_middle + 1
            assert 0 <= i_first <= len(array)
        elif array[i_middle] > search:
            i_last = i_middle - 1
            assert -1 <= i_last < len(array)

        # Found!
        else:
            assert array[i_middle] == search
            assert search in array
            return True

    assert not search in array
    # Not found!
    return False