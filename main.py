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

    #פונקציה המדפיסה את כמות הפעמים שאפשר לטעות בניחוש המילה וגם מדפיסה מסך פתיחה לתחילת המשחק




    #פונקציה המקבלת את הלשב בנוכחי במשחק, השלב זה כמות האותיות שהשחקן ניחש עד כה ומדפיסה מצב משחק מטעים


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
#פונקציה הבודקת האם הפלט שהוזן חוקי לפי חוקי המשחק האם האות היא תו חוקי האם זה אות בודדת ואם גן מחזיקה את האות


def is_valid_input(letter_guessed):


    if any(not x.isalpha() for x in letter_guessed) and len(letter_guessed) > 1:
        return False
    elif any(not x.isalpha() for x in letter_guessed):
        return False
    elif len(letter_guessed) > 1:
        return False
    else:
        return True

    # פונקציה הבודקת האם הפלט שהוזן חוקי לפי חוקי המשחק האם האות היא תו חוקי האם זה אות בודדת ומחזירה נכון אם האות חוקית ושקר אם האות לא חוקית


def generate_underscore_string(word):
    underscore_string = "_" * len(word)
    print(underscore_string)
    #פונקציה המקבלת את מילת המשחק ומדפיסה _ לפי אורך המילה



def check_valid_input(letter_guessed, old_letters_guessed):
    if not is_valid_input(letter_guessed):
        return False
    letter_guessed=letter_guessed.lower()
    if letter_guessed in old_letters_guessed:
        return False
    return True
#פונקציב שבודקת האם הקלט חוקי וגם הקלט לא שומש כבר בקלטים קודמים אם כן מחזיקה אמת אחרת שקר

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X\n")
        print(" -> ".join(old_letters_guessed))
        return False
    #פונקציה שמוסיפה את הקלט למערך הקלטים הקודמים אם הקלט חוקי ולא הופיעה כבר ומחזירה שקר אחת ומדפיס את התווים ששומשו שכבר נקלטו עד כה


def show_hidden_word(secret_word, old_letters_guessed):
    progress = ""

    for char in secret_word:
        if char in old_letters_guessed:
            progress += char
        else:
            progress += "_"

        progress += " "

    return progress.strip()
#פונקציה שמחזירה את מצב המשחק הנוכחי כל אות שהשחקן גילה היא מוסיפה וכל אות שהוא לא גילה מוסיפה _ במקום האות


def check_win(secret_word, old_letters_guessed):
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True
# פונקציה שבודקת האם השחקן ניצח לעומת רשימת התווים שנקלטו מול המילה שנבחרה במשחק

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

    #פונקציה המקבלת את הלשב בנוכחי במשחק, השלב זה כמות האותיות שהשחקן ניחש עד כה ומדפיסה מצב משחק מטעים


def choose_word(file_path, index):
    with open(file_path, 'r') as file:
        words = file.read().split()

    unique_words_count = len(set(words))

    circular_index = (index - 1) % len(words)

    return unique_words_count, words[circular_index]
#פונקציה שמקבלת קובץ ואינקדס מילה בקבוץ ומחזירה את המילה שנבחרה בוקבץ ואורך המילים בקובץ



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

# פונקציה מרכזית שממשת את כל שלבי המשחק מבקשת קלט מהמשתמש בודקת אם הוא חוקי ומוסיפה אותו לרשימת התווים שנקלטו
#אם הקלט לא חוקי המשתמש יתבקש לבחור קלט מחדש, בנוסף הפונקציה מעדכנת את מצב המשחק ומדפיסה אותו למשתמש
#הפונקציה בודקת אם המשתמש ניצח בכל תור ואם הוא ניצח או נגמר לא מספר הכשלונות ה=שהקוצו הפונקציה תדפיס את תוצאת המשחק

if __name__ == "__main__":
    main()


