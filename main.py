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
    guess = input("Please enter a letter (your guess): ")

    if any(not x.isalpha() for x in guess) and len(guess) > 1:
        return False
    elif not guess.isalpha():
        return False
    elif len(guess) > 1:
        return False
    else:
        return True


def generate_underscore_string():
    word = input("Please enter a word without spaces: ")
    underscore_string = "_" * len(word)
    print(underscore_string)




player_guess = get_guess()
start_game()
print_hangman(1)
generate_underscore_string()

