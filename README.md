# Number Guessing Game

A simple command-line number guessing game built with Python.

The player chooses a difficulty level, tries to guess a randomly generated number, and receives hints after each attempt.

## Features

* Three difficulty levels
* Randomly generated secret number
* Limited attempts based on difficulty
* "Too High" and "Too Low" hints
* Input validation for invalid numbers
* Option to play again
* Functions used to organize the program

## Difficulty Levels

| Difficulty | Number Range | Attempts |
| ---------- | ------------ | -------- |
| Easy       | 1–50         | 10       |
| Medium     | 1–100        | 7        |
| Hard       | 1–500        | 5        |

## How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone https://github.com/kiran-prabhu/number-guessing-game.git
```

Go into the project folder:

```bash
cd number-guessing-game
```

Run the game:

```bash
python main.py
```

## Technologies Used

* Python
* Python `random` module

## What I Learned

This project helped me practice:

* Variables
* `if / elif / else`
* `while` loops
* `try / except`
* `break` and `continue`
* Functions
* Parameters and arguments
* `return`
* Boolean values
* Input validation
* Basic program structure

## Future Improvements

Possible improvements for future versions:

* Add a scoring system
* Add a high-score system
* Add more difficulty levels
* Add hints based on the distance from the secret number
* Improve the user interface