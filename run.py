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

