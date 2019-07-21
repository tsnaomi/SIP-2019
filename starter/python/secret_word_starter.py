'''
------------------------ "GUESS THE SECRET WORD" GAME -------------------------

Your Mission (Should You Choose to Accept It):

    -   Complete the code where you see the numbered TODO comments below! :)

-------------------------------------------------------------------------------
'''
import random


# The main game function ------------------------------------------------------

def secret_word_game():
    ''' '''
    # Selects a random word using the function `get_random_word()`
    secret_word = get_random_word()

    # TODO 2: To set up the game, define the variable `masked_word` as the
    # value returned from calling the function `get_masked_word()`.
    # (HINT: Does `get_masked_word()` accept any arguments?)
    masked_word = 

    guesses = []    # for collecting guesses
    max_fails = 7   # maximum number of fails
    fails = 0       # number of fails

    # Prints the initial game state for the player to see! Note that the string
    # "\n" inserts a blank line!
    print(masked_word)
    print("Guess the secret word! You have", max_fails, "tries!\n")

    while fails < max_fails:

        # Collects a guess from the player.
        guess = input("Guess a letter: ")

        # TODO 4: Check if the guess is valid: Is it one letter? Has it
        # already been guessed? If so, cut the player some slack! Allow them to
        # guess again without losing a turn :)




        # Converts the guess to lowercase, so that it matches the case of the
        # secret word
        guess = guess.lower()

        # TODO 5: Check if the guess is correct: Is the letter in the word? If
        # so, unmask the guessed letter in `masked_word`!
        # (HINT: Use the function `unmask_letter()`!)




        # TODO 7: Check if the entire word has been revealed; if so, tell the
        # player they won! (Then end the game!)




        # TODO 8: If the guess is incorrect, update the number of fails.




        # TODO 9: Append the guess to the list of previous guesses.




        # Prints the current game state for the player to see!
        print(masked_word)
        print("Guesses thus far:", guesses)
        print("You have", max_fails - fails, "tries left!\n")

    # TODO 10: If the player doesn't guess the word in time, tell them they
    # lost. Perhaps even tell them the secret word!




# Helper functions ------------------------------------------------------------

def get_random_word():
    # TODO 1: Fill this list with fun words!
    potential_words = ["mafia", "angel", "detective", "peeker", "joker"]

    # Randomly selects a word from `potential_words`.
    word = random.choice(potential_words)

    # Converts `word` to lowercase.
    word = word.lower()

    # DEBUG: To preview the secret word, uncomment the following line:
    # print('Randomly selected word:', word)

    return word


def get_masked_word(word):
    '''Return a list of underscores that "masks" the letters in `word`.

    For example:

        INPUT               OUTPUT
        -------             -------------------------
        "dog"       ->      ["_", "_", "_"]
        "panda"     ->      ["_", "_", "_", "_", "_"]

    '''
    # TODO 3: Replace `pass` with the function code.
    # (HINT: This function should *return* a list of underscores!)
    pass


def unmask_letter(letter, secret_word, masked_word):
    '''Return `masked_word` with the value of `letter` unmasked.

    For example, if `letter` is "a" and `secret_word` is "cat", then the
    `masked_word` should change accordingly:

        INPUT                       OUTPUT
        ---------------             ---------------
        ["_", "_", "_"]     ->      ["_", "a", "_"]

    '''
    # TODO 6: Replace `pass` with the function code.
    # (HINT: This function should *return* a list of underscores and letters!)
    pass


# Launch the game! ------------------------------------------------------------

secret_word_game()
