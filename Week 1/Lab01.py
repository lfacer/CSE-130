# 1. Name: 
#    Lyndsey Facer
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    This is a guess the number game. The program will generate a 
#    random number and the user will enter numbers to guess the number
#    the program will alert the user whether their guess was too high
#    or too low. It will also let the user know how many guesses it
#    took.
# 4. What was the hardest part? Be as specific as possible.
#    For me this program wasn't very difficult. I had to refer to the 
#    python tutorial page a few times to remember how to format
#    a few things, but those were super simple things that I just
#    needed to double check. Other than than I found this program to be 
#    very simple.
# 5. How long did it take for you to complete the assignment?
#    This took me about an hour all together. 

import random

# Game introduction.
print("Welcome! This is the 'guess a number' game.")
print("Try and guess the number in the fewest attemps possible.")

# Prompt the user for how difficult the game will be. Ask for an integer.
value_max = int(input("Pick a positive number: "))

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
print(f"Guess a number between 1 and {value_max}.")

# Initialize the sentinal and the array of guesses.
user_guess = 0
user_guess_list = []

# Play the guessing game.
while user_guess != value_random:

    # Prompt the user for a number.
    user_guess = int(input("Guess: "))
    # Store the number in an array so it can be displayed later.
    user_guess_list.append(user_guess)

    # Make a decision: was the guess too high, too low, or just right.
    if user_guess > value_random:
        print("     Too high!")
    elif user_guess < value_random:
        print("     Too low!")

if user_guess == value_random:
    print("     You got it!")
# Give the user a report: How many guesses and what the guesses where.
print(f"You were able to find the number in {len(user_guess_list)} guesses.")
print(f"The numbers you guessed were: {user_guess_list}")
