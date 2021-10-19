import random
import string

from words import words
from hangman_visuals import lives_visual_dict


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    print(lives_visual_dict.get(lives))

    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left and You have used these letters:', ' '.join(used_letters))

        # what current word is
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(word_list)
        print('Current word: ', " ".join(word_list))

        user_letter = input('Guess a letter ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(lives_visual_dict.get(lives))
                print('Letter is not in the word.')
        elif user_letter in used_letters:
            print('You guessed the same letter')
        else:
            print('Invalid character!!')
    if lives == 0:
        print('GameOver!!! You suck at this game...')
    else:
        print('Congo you guessed the word: ', word)

hangman()