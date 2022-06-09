# 1. Name:
#      Lyndsey Facer
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program asks the user to enter the name of a file.
#      It then asks the user to enter a word within the file.
#      The program searches for the word by splitting the document in half,
#      and then continues to half it, until it either finds the word,
#      or runs out of options to look for the word.
# 4. Algorithmic Efficiency
#      I think that this program is a Linear or O(n) function. This is because
#      The main function of finding the word contains while and if loops.
#      Although many other functions are Constant, like reading the file,
#      As a whole, it is O(n).
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part was the main while loop for me. I only had a partial
#      understanding of how it was executed from class, so trying to program
#      it was pretty tricky for me.
# 6. How long did it take for you to complete the assignment?
#      This assignment took me about 2.5 hours to complete.


import json

# Asks for the name of the file.
names_text = input("What is the name of the file? ")

# Opens and reads the file, then turns it into an array.
with open(names_text) as f:
    names_json = json.load(f)
    names_list = names_json['array']

# Asks for the word you are searching for.
element = input("What name are you looking for? ")

# Sets the values for i_first, i_last, and found.
i_first = 0
i_last = len(names_list) - 1
found = False

# As long as the word hasn't been found, the loop will search for it.
while i_first <= i_last and found == False:
    i_middle = int((i_first + i_last) / 2)

    # This searches the first half.
    if names_list[i_middle] < element:
        i_first = i_middle + 1

    # This searches the last half.
    elif names_list[i_middle] > element:
        i_last = i_middle - 1

    # Once the program finds the word, it will print out found.
    else:
        found = True
        print("Found")

# If the program doesn't find the word, and reaches the end of the list,
# then it will end and print nothing.
print("\n")
