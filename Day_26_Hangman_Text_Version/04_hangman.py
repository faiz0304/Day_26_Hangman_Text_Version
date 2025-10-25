# Project: Hangman (Simple Text Version)
# Day: 26 - Python Mini Projects Series
# Week 4: OOP & Little Challenges
# Author: Faiz Ur Rehman Ashrafi

# Version: v4 (Final OOP Enhanced)
# Goal:
#   - Randomly select word from list.
#   - Give detailed user feedback.
#   - Use class-based approach with proper methods and conditions.

from typing import List
from random import choice


class Hangman:
    def __init__(self, word: str, chance: int = 5) -> None:
        self.word = word
        self.chance = chance
        self.guess_words: List[str] = []

    def display(self) -> None:
        """Show the current guessed letters and remaining lives."""
        for w in self.word:
            print(f" {w} " if w in self.guess_words else "_ ", end="")

        if self.chance > 0:
            print(f"\nYou have {self.chance} chance(s) left.\n")
        else:
            print("\nNo more chances left!")

    def check_guess(self, guess: str) -> None:
        """Check guessed letter and adjust state."""
        if guess in self.word:
            if guess not in self.guess_words:
                self.guess_words.append(guess)
                print(f"Perfect! '{guess}' is correct!")
            else:
                print("Oops! You already guessed that. -1 chance.")
                self.chance -= 1
        else:
            print("Wrong guess! -1 chance.")
            self.chance -= 1

    def check_guess_condition(self, guess: str):
        """Input validation and exit control."""
        if guess == "0":
            print("You chose to exit the game.")
            return "break"
        if len(guess) > 1:
            print("Please enter only ONE letter.")
            return "continue"
        if not guess.isalpha():
            print("Please enter alphabets A-Z only.")
            return "continue"

    def check_exit_condition(self):
        """Win or lose conditions."""
        if len(self.guess_words) == len(set(self.word)):
            print("\nCongratulations! You guessed the full word correctly!")
            return "break"
        if self.chance == 0:
            print(f"\nGame Over! The correct word was '{self.word}'.")
            return "break"


def main():
    """Main driver function to start the game."""
    print("=== Welcome to Hangman (Text Version) ===\n")

    words = ["hangman", "programming", "python"]
    word = choice(words)  # Randomly pick one word from list

    print(f"Word length = {len(word)}")
    print(" _ " * len(word))  # Display underscores

    play = Hangman(word)

    while True:
        print("\nType '0' to Exit.")
        guess = input("Guess a letter: ").lower().strip()

        # Check validity and control flow
        check = play.check_guess_condition(guess)
        if check == "break":
            break
        elif check == "continue":
            continue

        # Process guess and show game state
        play.check_guess(guess)
        play.display()

        # Check win/loss
        if play.check_exit_condition() == "break":
            break


if __name__ == "__main__":
    main()
