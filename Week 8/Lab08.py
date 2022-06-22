# 1. Name:
#      Lyndsey Facer
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      This program loads in a document and turns it into a list.
#      It then runs through the program and puts the list in order
#      alphabetically. It does this using three different functions:
#      i_pivot, i_largest, and i_check. Basically i_checker starts at 
#      the beginning of the list, and compares the largest number to 
#      the number at the end. If the number is larger than the last 
#      one it will swap the two. If it isn't, it will place that item 
#      right after the largest item. It does this, untill it reaches 
#      the end of the list.
# 4. What was the hardest part? Be as specific as possible.
#      I ran into some trouble with getting the for loops to work.
#      I didn't have the right range functions, so it kept ittering
#      through them incorrectly. But after I added a step, it worked.
# 5. How long did it take for you to complete the assignment?
#      This took me about 2.5 hours to complete.

import json

# Asks for the name of the file.
names_text = input("What is the name of the file? ")

# Opens and reads the file, then turns it into an array.
with open(names_text) as f:
    names_json = json.load(f)
    array = names_json['array']

    # Check if the array is a list.
    assert type(array) == list

# Goes through the array, starting with the largest number, and working
# backwards towards 0.
for i_pivot in range(len(array)-1,0,-1):
    assert 0 <= i_pivot <= len(array)
    i_largest = 0
    assert type(i_largest) == int

    # i_check starts at 0, and goes up through the highest number in the list.
    for i_check in range(0, i_pivot):
        assert 0 <= i_check <= i_pivot
        if array[i_check] > array[i_largest]:
            assert i_check > i_largest
            i_largest = i_check

    # Swaps the words in alphabetical order.
    if array[i_largest] > array[i_pivot]:
        array[i_largest], array[i_pivot] = array[i_pivot], array[i_largest]

# Prints out the sorted list.
print(f"The values in {names_text} are:")
print(*array, sep="\n")