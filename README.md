# Guess the Word

## Setup

We are running this program on [pythonanywhere.com](pythonanywhere.com)

## Code Helps

`import random`

- random is a library that lets the computer make choices for us

### Step 1: Create Variables

- Suggested variables:
  - A counter to track how many guesses we have left
  - A list of words
  - The secret word
  - A clue to display the parts of the word guessed
  - A symbol to make our counter fun
    - [Emojipedia](https://emojipedia.org/)
  - The game status

```python
guesses_left = 9
words = ['sunny', 'daisy', 'water', 'beach', 'green', 'music', 'porch', 'grill', 'flower']
secret_word = random.choice(words)
clue = list('?????')
heart_symbol = '💖'
guessed_word_correctly = False
```

### Step 2: Is guessed letter in the secret word?

- One possible function:
  - Loop through each character of the secret word
  - Condition to update the clue

```python
def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1
```

### Step 3: Clean up Clue Display

- One possible function:
  - `print(clue)` displays `[‘?’, ‘?’, ‘?’, ‘?’, ‘?’]`
  - The function below converts `clue` to a single string (`?????` is much prettier)

```python
def listToString(my_list):
    cluestring = ' '
    return (cluestring.join(my_list))
```

### Step 4: Game Play

- Keep guessing until we’re out of turns
  - Display the clue
  - Display how many guesses the user has left
  - Ask the user for a guess

```python
print('Guess the word associated with Summer!')
while guesses_left > 0:
    print(listToString(clue))
    print('Guesses left: ' + heart_symbol * guesses_left)
    guess = input('Guess a letter or the whole word: ')
```

### Step 5:  Check the guess Part 1

- Be sure to indent this code so it is part of the main program ("while loop")
- Did they guess the word?
  - If yes, update game status

```python
if guess == secret_word:
    guessed_word_correctly = True
    break
```

### Step 6: Check the guess Part 2

- Be sure to indent this code so that it is part of the game play code ("while loop")
- Is the guess a letter in the secret word?
  - If yes, use the function we created to update the clue
  - If no, lower the guesses left

```python
if guess in secret_word:
    update_clue(guess, secret_word, clue)
else:
    print('Incorrect. You lose a life')
    guesses_left = guesses_left - 1
```

### Step 7: Update game status

- If following along using the sample code, don’t indent this section
  - It will only run after the user is done guessing (outside of the "while loop")
- Tell the user if they won or lost

```python
if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
else:
    print('You lost! The secret word was ' + secret_word)
```

### Other things to try

- Different words
- Different word lengths
- Use a different symbol
- Change the number of guesses

### Notes

This lesson was based on Nine Lives from Coding Projects in Python
and borrowed from [Lakewood Girls Who Code](https://sites.google.com/view/gwc-lpl).
