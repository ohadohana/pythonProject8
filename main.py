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

    MAX_TRIES = 6

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

def choose_word(file_path, index):
    with open(file_path, 'r') as file:
        words = file.read().split()

    unique_words_count = len(set(words))

    circular_index = (index - 1) % len(words)

    return unique_words_count, words[circular_index]



def main():
    start_game()
    file_path = input("Please enter file path: ")
    index = int(input("Please enter an index of a word: "))
    unique_words_count, word = choose_word(file_path, index)
    guees_letter=""
    Hidden_word=show_hidden_word(word,[""])
    print(Hidden_word)
    old_letters=[]
    Valid=False
    won=False
    counter_of_succeus=0
    num_of_faults=6
    print_hangman(counter_of_succeus)
    while won==False and num_of_faults>0:
        guees_letter = input("guess a letter")
        Valid=try_update_letter_guessed(guees_letter,old_letters)
        while Valid==False:
            guees_letter = input("guess a letter")
            Valid = try_update_letter_guessed(guees_letter, old_letters)
        if guees_letter in word:
            counter_of_succeus+=1
        else:
            num_of_faults-=1
            print(":(")
        print_hangman(counter_of_succeus)
        print(show_hidden_word(word,old_letters))
        won=check_win(word,old_letters)

    if won==True:
        print("you won")
    else:
        print("you lost")

main()



