## =============================
##     IMPORT STATEMENT(S)
## =============================

import random
from typing import List


## =============================
##          CONSTANTS
## =============================

WORD_BANK = [
    'sunny','daisy','water', 'beach',
    'green','music','porch','grill','flower'
    ]
GUESSES_SYMBOL = "🌞"

## =============================
## STRING MANIPULATION FUNCTIONS
## =============================


def update_clue(
    clue: str,
    secret_word: str,
    guessed_letter: str
    ) -> str:
    '''Update clue with correctly guessed letters'''

    # The version we prefer
    for letter_index, correct_letter in enumerate(secret_word):
        if guessed_letter == correct_letter:
            clue[letter_index] = guessed_letter

    # # The original version
    # index = 0
    # while index < len(secret_word):
    #     if guessed_letter == secret_word[index]:
    #         clue[index] = guessed_letter
    #     index += 1

    return clue


def listToString(mylist: List[str]) -> str:
    cluestring = ' '
    return cluestring.join(mylist)


## =============================
##     GAME PLAY FUNCTIONS
## =============================


def game_over(word: str, *, winner: bool) -> None:
    '''End the game'''
    if winner:
        print(f"You win!  The secret word was {word}")
    else:
        print(f"You lose! Womp, womp.  The secret word was {word}")


def main() -> None:
    '''Play the '''
    guesses_left = 9
    super_secret_word = random.choice(WORD_BANK)
    not_so_secret_clue = list('?????')
    guessed_word_correctly = False
    print("Guess the word associated with Summer! ")

    while guesses_left > 0:

        # Get a clue!
        print(listToString(not_so_secret_clue))
        print(f"Guesses left: {GUESS_SYMBOL * guesses_left}")

        # Make a guess!
        guess = input("Guess a letter or the whole word: ")

        # Evaluate.
        if guess == super_secret_word:
            # We won!
            game_over(super_secret_word, winner=True)
            return

        if guess in super_secret_word:
            # We're getting closer!
            not_so_secret_clue = update_clue(not_so_secret_clue, super_secret_word, guess)

        else:
            # Uh oh.
            print('Incorrect. You lose a life!')
            guesses_left = guesses_left - 1

    # We're out of guesses. Womp wah.
    game_over(super_secret_word, winner=False)


## =============================
##       "Dunder main"
## =============================


if __name__ == '__main__':
    main()
