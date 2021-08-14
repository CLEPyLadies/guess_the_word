import random
from typing import Iterable, Optional


SUMMER_WORDS = ['sunshine', 'surfboard', 'dog-days', 'beach', 'hot', 'concerts', 'porch sitting', 'grill', 'flowers']


class GuessingGame:
    '''Stateful object for "guess the word" game'''
    
    def __init__(
        self, n_guesses: int, word_bank: Iterable[str]
        ):
        self.guesses_left = n_guesses
        self.word_bank = word_bank
        self.guesses_symbol = "🤔"
        # These will be populated later
        self.secret_word = ''
        self.clue = ''

    def set_secret_word(self, *, secret: Optional[str] = None):
        '''Set the secret word'''

        if isinstance(secret, str) and (len(secret) > 1):
            self.secret_word = secret
        else:
            self.secret_word = random.choice(self.word_bank)
        
        self.populate_clue()

    def populate_clue(self):
        '''Create an emoji version of the secret word'''

        for char in self.secret_word:
            if char.isalpha():
                self.clue += self.guesses_symbol
            else:
                self.clue += char
        print(f'Initial clue is {self.clue}')

    def update_clue(self, guess: str) -> None:
        '''Update the clue string'''
        for letter_position, correct_letter in enumerate(self.secret_word):
            if guess == correct_letter:
                self.clue[letter_position] = guess


def main():
    '''Controller'''
    print('Let\'s make a game!')
    game_play = GuessingGame(9, SUMMER_WORDS)
    game_play.set_secret_word()


if __name__ == '__main__':
    main()
