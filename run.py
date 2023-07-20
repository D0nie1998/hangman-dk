import random
import sys
import os
import operator

import gspread
from google.oauth2.service_account import Credentials

from words import word_list



game_results = {}

current_word = ''
masked_word = ''


def clear_terminal():
    """
    Clears the terminal and code sourced from:
    http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf
    """
    os.system('cls' if os.name == 'nt' else 'clear')




def get_word():
    word = random.choice(word_list)
    return word.upper()

def welcome_screen():
    clear_terminal()
    print("Let's")
    print(" _ _ _ _ _ ____ _ ")
    print(" | | | | / \ | \ | |/ __| __ ___ __ _ _ __ | |")
    print(" | || | / _ \ | \| | | _| ' ` _ \ / ` | ' \ | | ")
    print(" | _ |/ ___ \| |\ | |_| | | | | | | (_| | | | ||_|")
    print(" |_| |_/_/ \_\_| \_|\____|_| |_| |_|\__,_|_| |_|(_)")
    print()
    print("\n" * 2)
    print("{:^70}".format("1: PLAY GAME"))
    print("{:^70}".format("3: EXIT"))
    print("\n" * 3)

    while True:
        welcome_screen_choice = input("  " * 11 + "Please choose an option : ")
        if welcome_screen_choice == "1":
            player_name()
        elif welcome_screen_choice == "3":
            clear_terminal()
            sys.exit()
        else:
            print("{:^70}".format("Please Choose option 1, 2 or 3"))

def player_name():
    clear_terminal()
    attempts = 0
    print("{:^78}".format("WELCOME TO HANGMAN!"))
    print(show_hangman(attempts))
    print(letters_box)
    global player
    letters_box2 = letters_box
    while True:
        player = input("  " * 10 + " Please enter a Username: ").upper()
        if player.isalpha():
            game_results[player] = 0
            play(get_word(), letters_box2)
        else:
            print("{:^74}".format("Please use letters only"))

        def replace_guess(word, masked_word, guess):
    index = 0
    masked_word = list(masked_word)
    for letter in word:
        if letter.upper() == guess.upper():
            masked_word[index] = guess
        index = index + 1
    return ''.join(masked_word)

    def check_if_guess_in_word(guess, word):
    return guess.upper() in word.upper()


def validate_guess(guess, guessed_letters):
    if (len(guess) == 1) and guess.isalpha() and (
       guess not in guessed_letters):
        return True
    if guess in guessed_letters:
        print("You've already guessed the letter: " + guess)
    if guess.isalpha() is False:
        print("Guess is not valid, please try again.")
    return False