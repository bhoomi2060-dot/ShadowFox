import random

# Word bank with hints
word_bank = {
    "python": "A popular programming language named after a snake",
    "computer": "An electronic device used for processing data",
    "elephant": "The largest land animal on Earth",
    "guitar": "A musical instrument with strings",
    "mountain": "A large natural elevation of the earth's surface",
    "keyboard": "A device used to type on a computer",
    "rainbow": "A colorful arc seen in the sky after rain",
    "diamond": "A precious gemstone known for its hardness"
}

# ASCII art stages for the hangman (7 wrong guesses allowed = 6 stages + full)
hangman_stages = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """
]


def choose_word():
    word = random.choice(list(word_bank.keys()))
    hint = word_bank[word]
    return word, hint


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word, hint = choose_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = len(hangman_stages) - 1
    hint_used = False

    print("\n" + "=" * 40)
    print("       WELCOME TO HANGMAN")
    print("=" * 40)
    print(f"\nThe word has {len(word)} letters.")
    print("Type a letter to guess, or 'hint' for a clue.\n")

    while wrong_guesses < max_wrong_guesses:
        print(hangman_stages[wrong_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Wrong guesses remaining: {max_wrong_guesses - wrong_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word: " + word.upper())
            return

        guess = input("\nEnter a letter (or 'hint'): ").lower().strip()

        # Hint option
        if guess == "hint":
            if not hint_used:
                print(f"\n💡 Hint: {hint}")
                hint_used = True
            else:
                print("\nYou've already used your hint for this game!")
            continue

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("\nPlease enter a single letter.")
            continue

        if guess in guessed_letters:
            print("\nYou already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"\nGood guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"\nSorry, '{guess}' is not in the word.")

        print()

    # Game over - lost
    print(hangman_stages[wrong_guesses])
    print(f"💀 Game over! You've run out of guesses.")
    print(f"The word was: {word.upper()}")


def main():
    play_again = "yes"
    while play_again.lower() in ["yes", "y"]:
        play_hangman()
        play_again = input("\nPlay again? (yes/no): ").strip()
        print()
    print("Thanks for playing Hangman! Goodbye. 👋")


if __name__ == "__main__":
    main()