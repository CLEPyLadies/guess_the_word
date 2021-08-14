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
        self.player_won = None

    @property
    def is_in_progress(self) -> int:
        '''Property to check game play remaining'''
        if self.player_won:
            return 0
        return self.guesses_left
    
    def set_secret_word(self, *, secret: Optional[str] = None):
        '''Set the secret word'''

        if isinstance(secret, str) and (len(secret) > 1):
            self.secret_word = secret
        else:
            self.secret_word = random.choice(self.word_bank)
        
        self.populate_clue()

    def populate_clue(self) -> None:
        '''Create an emoji version of the secret word'''

        for char in self.secret_word:
            if char.isalpha():
                self.clue += self.guesses_symbol
            else:
                self.clue += char
        print(f'Initial clue is {self.clue}')

    def update_clue(self, guess: str) -> None:
        '''Update the clue string'''
        tmp_clue = self.clue
        self.clue = ''
        for clue_letter, correct_letter in zip(tmp_clue, self.secret_word):
            if guess == correct_letter:
                self.clue += guess
            else:
                self.clue += clue_letter

    def check(self, guess: str):
        '''Check a guess'''

        self.update_clue(guess)

        guessed_word = guess == self.secret_word
        completed_clue = self.clue == self.secret_word
        if guessed_word or completed_clue:
            self.player_won = True
            return

        print('Incorrect. You lose a life!')
        self.guesses_left -= 1
        return
    
    def take_a_turn(self):
        '''Play a single turn'''

        print('\tCurrent clue:', self.clue)
        print(f'\tGuesses left: {self.guesses_symbol * self.guesses_left}')

        guess = input('Guess a letter or the whole word. ')
        self.check(guess)

    def game_over(self):
        '''Game over message'''
        if self.player_won:
            print(
                "You win! The secret word was ",
                self.secret_word
                )
        else:
            print(
                "You lose! Womp, womp.  The secret word was ",
                self.secret_word
                )


def main():
    '''Controller'''
    print('Let\'s make a game!')
    game_play = GuessingGame(9, SUMMER_WORDS)
    game_play.set_secret_word()
    while game_play.is_in_progress:
        game_play.take_a_turn()
    game_play.game_over()


if __name__ == '__main__':
    main()
