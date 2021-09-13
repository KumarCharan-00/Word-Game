"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    word = list(secret_word)
    # print(word)
    lst = ['-'] * len(word)
    guesses = INITIAL_GUESSES
    char = '-'
    while game_status(lst) or guesses > 0:
        print("You have " + str(guesses) + " guesses left")
        char = input("Type a single letter here, then press enter: ").upper()
        if len(char) != 1:
            print("Guess should only be a single character.")
        elif char not in word:
            print("There are no " + char + "'s in the word")
            guesses -= 1
        else:
            lst = update_game_status(char, lst, word)

    if '-' in lst:
        print("Sorry, you lost. The secret word was:", secret_word)
    else:
        print("Congratulations, the word is:", secret_word)

def game_status(lst):
    print("The word now looks like this:", "".join(lst))
    return True if '-' in lst else False

def update_game_status(char, lst, word):
    if char in word and char not in lst:
        print("That guess is correct.")
    for i in range(len(word)):
        if word[i] == char and lst[i] != char:
            lst[i] = word[i]
    return lst

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    open_file = open("Lexicon.txt", "r")
    lines = open_file.readlines()
    words = []
    for line in lines:
        words.append(line.strip())
    index = random.randrange(len(words))
    return words[index]

def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
