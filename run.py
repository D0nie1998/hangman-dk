import random
import sys
import os
import operator


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
    print("{:^70}".format("2: EXIT"))
    print("\n" * 3)

    while True:
        welcome_screen_choice = input("  " * 11 + "Please choose an option : ")
        if welcome_screen_choice == "1":
            player_name()
        elif welcome_screen_choice == "3":
            clear_terminal()
            sys.exit()
        else:
            print("{:^70}".format("Please Choose option 1"))


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


def play(word, letters_box):
    letters_box2 = letters_box
    clear_terminal()
    completed_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    attempts = 7
    print(show_hangman(attempts))
    print(letters_box2)
    print(completed_word)
    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == len(word):
            if check_if_guess_in_word(guess, word) is False:
                print("Sorry " + guess + " is not the word.")
                attempts -= 1
            else:
                guessed = True
        else:
            if validate_guess(guess, guessed_letters):
                guessed_letters.append(guess)
                letters_box2 = letters_box2.replace(guess.upper(), '*')
                if check_if_guess_in_word(guess, word):
                    completed_word = replace_guess(word, completed_word, guess)
                    print("Well done!", guess, "is in the word.")
                    if completed_word.upper() == word.upper():
                        guessed = True
                else:
                    print("Sorry " + guess + " is not in the word.")
                    attempts -= 1
            else:
                if guess.isalpha():
                    letters_box2 = letters_box2.replace(guess.upper(), '*')
                if check_if_guess_in_word(guess, completed_word) is False:
                    attempts -= 1
        print(show_hangman(attempts))
        print(letters_box2)
        print(completed_word)
    if guessed:
        clear_terminal()
        print("Congratulations! " + player +
              ", you guessed the word correctly! You Win!")

        while True:
            play_again_after_win = input('  ' * 10 +
                                         ' Play Again? ( Y / N ) : ').upper()
            if play_again_after_win == 'Y':
                play(get_word(), letters_box)
            elif play_again_after_win == 'N':
                welcome_screen()

    else:
        print("Sorry " + player + ", you died")
        print("the word was " + word + ", better luck next time!")

        while True:
            play_again_after_lose = input('  ' * 10 +
                                          ' Play Again? ( Y / N ) : ').upper()
            if play_again_after_lose == 'Y':
                play(get_word(), letters_box)
            elif play_again_after_lose == 'N':
                welcome_screen()
            else:
                print('{:^70}'.format(' Please choose option Y or N '))


def show_hangman(attempts):
    phases = [
                """
                    +---------------------------------+
                    |             HANGMAN             |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                O                |
                    |               /|\\               |
                    |               / \\               |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |             HANGMAN             |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                O                |
                    |               /|\\               |
                    |               /                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |             HANGMAN             |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                O                |
                    |               /|\\               |
                    |                                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |             HANGMAN             |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                O                |
                    |               /|                |
                    |                                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |             HANGMAN             |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                O                |
                    |                |                |
                    |                                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |             HANGMAN             |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                O                |
                    |                                 |
                    |                                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |             HANGMAN             |
                    |           +---------+           |
                    +---------------------------------+
                    |                |                |
                    |                |                |
                    |                                 |
                    |                                 |
                    |                                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+""",
                """
                    +---------------------------------+
                    |             HANGMAN             |
                    |           +---------+           |
                    +---------------------------------+
                    |                                 |
                    |                                 |
                    |                                 |
                    |                                 |
                    |                                 |
                    |          +------------+         |
                    |          |            |         |
                    +---------------------------------|
                    |        Available letters        |
                    +---------------------------------+"""
                ]
    return phases[attempts]


letters_box = """                    |    A B C D E F G H I J K L M    |
                    |    N O P Q R S T U V W X Y Z    |
                    |                                 |
                    +---------------------------------+
    """


def main():
    letters_box2 = letters_box
    welcome_screen()
    current_word = get_word()
    play(current_word, letters_box2)
    while input("Play again? (Y/N) ").upper() == "Y":
        letters_box2 = letters_box
        word = get_word()
        play(word, letters_box2)
        welcome_screen()


if __name__ == "__main__":
    main()
