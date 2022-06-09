# SWAP
# data = ["alpha", "beta", "gamma", "omega"]
# data[2], data[3] = data[3], data[2]
# print(data)

def average_gpa(gpas):

    assert type(gpas) == list

    sum = 0
    for gpa in gpas:
        assert gpa >= 0.0, "GPA cannot be negative."
        assert gpa <= 4.0, "Nothing greater than 4.0"
        assert type(gpa) == int or type(gpa) == float
        sum += gpa

    assert len(gpas) > 0, "We are about to divide by zero!"
    average = sum / len(gpas)

    assert average <= sum
    assert average >= 0.0, "No negative GPAs"
    assert average <= 4.0, "Average should be a valid GPA"
    return average


def linear_search(array, search):

    assert type(array) == list
    assert len(array) >= 0
    assert search != None

    for index in range(0, len(array)):

        assert 0 <= index < len(array)
        assert type(array[index]) == type(search)


        if array[index] == search:
            return True
    return False