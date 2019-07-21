# Imports the ability to get a random number.
# (We will learn more about this later!)
import random

# Generates a random integer.
random_number = random.randint(1, 20)

# DEBUG: To preview the random number, uncomment the following below:
# print(random_number)

guess = input("Guess a number between 1 and 20 (inclusive): ")

if not guess.isnumeric():  # Checks if the guess consists only of digits.
    print("That's not a positive whole number, try again!")

else:
    guess = int(guess)  # Converts the string into the integer data type.
