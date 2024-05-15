import random

def start_game():
    HANGMAN_ASCII_ART=  "Welcome to the game Hangman.\n"
    hangman_text = """
     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/                      
    """

    MAX_TRIES = random.randint(5, 10)

    print(hangman_text)
    print(f"Number of attempts allowed: {MAX_TRIES}")


def print_hangman(step):
    hangman_pics = [
        """
        x-------x
        """,
        """
        x-------x
        |
        |
        |
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
        """,
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        """
    ]

    print(hangman_pics[step])


def get_guess():
    guess = input("Please enter a letter (your guess): ")

    if any(not x.isalpha() for x in guess) and len(guess) > 1:
        print("E3")
    elif not guess.isalpha():
        print("E2")
    elif len(guess) > 1:
        print("E1")
    else:
        if guess.isupper():
            guess = guess.lower()
        print(guess)
        return guess

    return None


def is_valid_input(letter_guessed):


    if any(not x.isalpha() for x in letter_guessed) and len(letter_guessed) > 1:
        return False
    elif any(not x.isalpha() for x in letter_guessed):
        return False
    elif len(letter_guessed) > 1:
        return False
    else:
        return True


def generate_underscore_string():
    word = input("Please enter a word without spaces: ")
    underscore_string = "_" * len(word)
    print(underscore_string)

def check_valid_input(letter_guessed, old_letters_guessed):
    if not is_valid_input(letter_guessed):
        return False
    letter_guessed=letter_guessed.lower()
    if letter_guessed in old_letters_guessed:
        return False
    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X\n")
        print(" -> ".join(old_letters_guessed))
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    progress = ""

    for char in secret_word:
        if char in old_letters_guessed:
            progress += char
        else:
            progress += "_"

        progress += " "

    return progress.strip()

def check_win(secret_word, old_letters_guessed):
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True

def print_hangman(num_of_tries):
    hangman_pics = [
        """
        x-------x
        """,
        """
        x-------x
        |
        |
        |
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        """,
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
        """,
        """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        """
    ]

    print(hangman_pics[num_of_tries])

secret_word = "mammals"
old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
print(show_hidden_word(secret_word, old_letters_guessed))
print(check_win(secret_word,old_letters_guessed))
print(print_hangman(4))




print(try_update_letter_guessed("a",{"a","b","c"}))
# player_guess = get_guess()
# start_game()
# print_hangman(1)
# generate_underscore_string()

