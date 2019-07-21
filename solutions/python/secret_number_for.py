# Challenge 2: Create a Guess the Number game with a for-loop and limit the
# player to three tries. Tell them if they should guess higher or lower next
# time.

# Imports the ability to get a random number.
# (We will learn more about this later!)
import random

# Generates a random integer.
random_number = random.randint(1, 20)

# DEBUG: To preview the random number, uncomment the following below:
# print(random_number)

for guess_number in range(3):
    guess = input("Guess a number between 1 and 20 (inclusive): ")

    if guess == str(random_number):
        print('You won!')
        break

    if guess_number == 2:
        print('You lost! Correct answer:', random_number)
        break

    if guess.isnumeric():  # Checks if the guess consists only of digits.
        guess = int(guess)  # Converts the string into the integer data type.

        if guess < random_number:
            print('Guess higher.')

        else:
            print('Guess lower.')

    else:
        print("That's not a positive whole number!")
