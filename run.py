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
