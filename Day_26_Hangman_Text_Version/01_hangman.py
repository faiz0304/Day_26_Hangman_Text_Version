# Project: Hangman (Simple Text Version)
# Day: 26 - Python Mini Projects Series
# Week 4: OOP & Little Challenges
# Author: Faiz Ur Rehman Ashrafi

# Version: v1 (Prototype)
# Goal:
#   - Understand core logic of Hangman.
#   - Guess letters in the word.
#   - Display guessed and hidden letters dynamically.

word = "hangman"  # The secret word to guess
print(" _ " * len(word))  # Show underscores for each letter (initial display)
guess_words = []  # Stores correctly guessed letters

while True:
    guess = input("\nGuess a word: ").lower().strip()

    # Check if the guessed letter is in the word
    if guess in word:
        if guess not in guess_words:
            guess_words.append(guess)  # Add only if not already guessed

    # Display the updated word progress
    for w in word:
        if w in guess_words:
            print(f" {w} ", end="")
        else:
            print(" _ ", end="")

    # When all unique letters guessed, end the game
    if len(guess_words) == len(set(word)):
        print("\nYes, you completed the word!")
        break
