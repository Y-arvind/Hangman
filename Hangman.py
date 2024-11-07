import random
from words import words
import string


def valid_word(word):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        word = word.upper()

    return word


def hangman():
    word = valid_word(words).upper()
    word_letters = set(word) # letters in the word

    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user guess
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f'lives: {lives}')
        print('You have used this letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print('current word: ', ' '.join(word_list))
        # getting user input
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:
            print("You have already used this letter")
        else:
            print("Invalid Character")
    if lives > 0:
        print(f"{word}  yeah you won !!")
    else:
        print(f"{word}  you lost!!")
hangman()