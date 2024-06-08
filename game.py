import random
import string

def get_word():
    """
    Returns a random word from the word list
    """
    word_list = ['python', 'programming', 'computer', 'science', 'algorithm']
    return random.choice(word_list)

def print_hangman(attempts):
    """
    Prints the hangman diagram based on the remaining attempts
    """
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    print(stages[attempts])

def play_hangman():
    word = get_word()
    word_letters = set(word)  # Set of letters in the word
    alphabet = set(string.ascii_lowercase)  # Set of all letters in the alphabet
    used_letters = set()  # Set of letters the user has guessed

    attempts = 6

    while len(word_letters) > 0 and attempts > 0:
        print(f"You have {attempts} attempts left.")
        print_hangman(attempts)

        # Get user input
        user_letter = input("Guess a letter: ").lower()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                attempts -= 1
                print("Letter is not in the word.")
        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")
        else:
            print("Invalid input. Please enter a single letter.")

    if attempts == 0:
        print(f"You ran out of attempts. The word was '{word}'.")
    else:
        print(f"Congratulations! You guessed the word '{word}'!")

play_hangman()