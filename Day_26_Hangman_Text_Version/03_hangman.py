# Project: Hangman (Simple Text Version)
# Day: 26 - Python Mini Projects Series
# Week 4: OOP & Little Challenges
# Author: Faiz Ur Rehman Ashrafi

# Version: v3 (OOP Structure)
# Goal:
#   - Convert procedural code into a class-based structure.
#   - Maintain clean methods for checking and displaying progress.

from typing import List


class Hangman:
    def __init__(self, word: str, chance: int = 5) -> None:
        self.word = word
        self.chance = chance
        self.guess_words: List[str] = []

    def display(self) -> None:
        """Display current progress and remaining chances."""
        for w in self.word:
            print(f" {w} " if w in self.guess_words else "_ ", end="")
        print(f"\nYou have {self.chance} chance(s) left.\n")

    def check_guess(self, guess: str) -> None:
        """Handle logic for right or wrong guesses."""
        if guess in self.word:
            if guess not in self.guess_words:
                self.guess_words.append(guess)
            else:
                print("\nYou already guessed that letter!")
        else:
            self.chance -= 1

    def check_guess_condition(self, guess: str):
        """Validate input and handle exit/continue logic."""
        if guess == "0":
            print("\nYou chose to exit.")
            return "break"
        if len(guess) > 1:
            print("\nPlease enter only ONE letter at a time.")
            return "continue"
        if not guess.isalpha():
            print("\nPlease enter alphabets A-Z only.")
            return "continue"

    def check_exit_condition(self):
        """Check for win or loss conditions."""
        if len(self.guess_words) == len(set(self.word)):
            print("\nCongratulations! You guessed the word!")
            return "break"
        if self.chance == 0:
            print("\nNo chances left! Game Over.")
            return "break"


def main():
    print("Welcome to Hangman (Text Version)")
    play = Hangman("hangman")

    while True:
        print("\nType '0' to Exit.")
        guess = input("\nGuess a letter: ").lower().strip()

        # Check input validity
        condition = play.check_guess_condition(guess)
        if condition == "break":
            break
        elif condition == "continue":
            continue

        # Update and show result
        play.check_guess(guess)
        play.display()

        # Check if player won or lost
        if play.check_exit_condition() == "break":
            break


if __name__ == "__main__":
    main()
