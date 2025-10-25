# Hangman (Simple Text Version)

**Day:** 26  
**Week:** 4 – OOP & Little Challenges  
**Project Name:** Hangman (Text Version)  
**Author:** Faiz Ur Rehman Ashrafi  

---

## Overview

This project is a **console-based Hangman game** where the player guesses a hidden word letter by letter.  
Each wrong guess reduces the number of available chances. The game continues until the player either guesses the word correctly or runs out of lives.

The project demonstrates step-by-step development — from a **basic prototype** to a **clean OOP implementation** using Python classes and methods.

---

## Game Logic

- A secret word is chosen (randomly in the final version).
- Each correct letter guess reveals that letter in the word.
- Incorrect guesses decrease your total remaining chances.
- Player wins when all letters are correctly guessed.
- Player loses when no chances remain.

---

## How to Play

1. Run the game file (`04_hangman.py` recommended).  
2. The game shows blanks (`_`) for the hidden word.  
3. Type one alphabet at a time to guess.  
4. You have **5 total chances**.  
5. Type **0** anytime to **exit** the game.

---

## Versions Overview

| File Name       | Version | Description |
|-----------------|----------|--------------|
| `01_hangman.py` | v1 | Basic prototype for core logic testing |
| `02_hangman.py` | v2 | Functional non-OOP version with validation and chances |
| `03_hangman.py` | v3 | First OOP structured version |
| `04_hangman.py` | v4 | Final version — OOP + random word + clean UX |

---

## Concepts Used

- Loops and conditionals  
- Lists and string operations  
- Input validation  
- Random word selection (`random.choice()`)  
- OOP (Classes, Methods, Attributes)

---

## Example Run

=== Welcome to Hangman (Text Version) ===

Word length = 7

Type '0' to Exit.
Guess a letter: a
Perfect! 'a' is correct!
_ a _ _ _ a _
You have 5 chance(s) left.

Guess a letter: n
Perfect! 'n' is correct!
_ a n _ _ a n
You have 5 chance(s) left.

Congratulations! You guessed the full word correctly!

---

## End Note

This project is part of **Faiz Ur Rehman Ashrafi’s Python Mini Projects Series**, focusing on daily coding discipline, logic building, and OOP fundamentals.

Day: 26 | Week: 4 | Project: Hangman (Text Version)

---

**© 2025 Faiz Ur Rehman Ashrafi – All Rights Reserved**