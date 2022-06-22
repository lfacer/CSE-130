# 1. Name:
#      Lyndsey Facer
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      This program asks the user for a number, and it will run
#      through the Francois sequence of numbers, and return the 
#      number in that location.
# 4. What was the hardest part? Be as specific as possible.
#      For me, finding the most effiecent possible solution.
#      Based on the pseudocode answers, I orignally had the 
#      second least effiecent answer. It totally worked fine, 
#      but while settle? So I focused on the most effiecent 
#      method.
# 5. How long did it take for you to complete the assignment?
#      Between my two versions on the code, it took about 1.5 hours.

# Asks the user for input, if the input isn't valid loops untill a 
# valid answer.
while True:

    number = int(input("Which Francois number would you like to see? "))
    if number <= 0:
        print("Please enter a valid number")
    else:
        break
    
# Sets up the array.
array = [1,2]

# Goes through the array, only using the necessary numbers in the array.
if number > 2:
    for index in range (3, number+1):
        array[index % 2] = array[0] + array[1]

# Prints out the value.
value = array[number % 2]
print(f"Francois number {number} is {value}")
