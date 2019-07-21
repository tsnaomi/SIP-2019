# Challenge 1: Create a Guess the Number game using a while-loop and limit the
# player to three tries. Tell them if they should guess higher or lower next
# time.

# Imports the ability to get a random number.
# (We will learn more about this later!)
import random

# Generates a random integer.
random_number = random.randint(1, 20)

# DEBUG: To preview the random number, uncomment the following below:
# print(random_number)

# Keep track of the number of guesses
number_of_guesses = 0

while number_of_guesses < 3:
    guess = input("Guess a number between 1 and 20 (inclusive): ")

    if guess.isnumeric():  # Checks if the guess consists only of digits.
        guess = int(guess)  # Converts the string into the integer data type.

        number_of_guesses += 1

        if guess == random_number:
            print("Woah, dude. You won.")
            break

        elif number_of_guesses == 3:
            print("Sorry, the correct number was", random_number)

        elif guess < random_number:
            print("Guess higher.")

        else:
            print("Guess lower.")

    else:
        print("That's not a positive whole number. Dude, try again!")
