# Project: Hangman (Simple Text Version)
# Day: 26 - Python Mini Projects Series
# Week 4: OOP & Little Challenges
# Author: Faiz Ur Rehman Ashrafi

# Version: v2 (Functional Complete)
# Goal:
#   - Add chances system and input validation.
#   - Show wrong guesses and exit condition.

print("Welcome to Hangman (Text Version)")

word = "hangman"  # Word to guess
print(" _ " * len(word))  # Initial display
guess_words = []  # List of correctly guessed letters
chance = 5  # Total chances to make mistakes

while True:
    print("\nType '0' to Exit the game.")
    guess = input("\nGuess a letter: ").lower().strip()

    # Exit condition
    if guess == "0":
        print("\nYou chose to exit the game. Goodbye!")
        break

    # Input validation (one alphabet only)
    if len(guess) > 1:
        print("\nPlease enter only ONE letter at a time.")
        continue
    if not guess.isalpha():
        print("\nPlease enter alphabets A-Z only.")
        continue

    # Correct guess
    if guess in word:
        if guess not in guess_words:
            guess_words.append(guess)
        else:
            print("\nYou already guessed that letter!")

    # Wrong guess
    elif guess not in word:
        chance -= 1
        print("\nWrong guess! You lost one chance.")

    # Show progress
    for w in word:
        print(f" {w} " if w in guess_words else "_ ", end="")

    print(f"\nYou have {chance} chance(s) left.\n")

    # Check win or lose conditions
    if len(guess_words) == len(set(word)):
        print("\nCongratulations! You guessed the word correctly!")
        break
    elif chance == 0:
        print("\nBetter luck next time! The word was:", word)
        break
