
# Coin Grab Game

## Overview

"Coin Grab" is a simple logic game developed in Python without a graphical interface. Two players, a human player, and a computer, take turns grabbing coins with the aim of avoiding being the one to take the last coin. The game is designed to challenge players' strategy and logic skills.

## Rules

1. The game starts with a specified number of coins, typically 15.
2. On each turn, players can choose to take from one to three coins.
3. The player who takes the last coin loses the game.

## How to Play

To play the game, follow these steps:

1. Run the Python script using an interpreter (e.g., `python coin_grab_game.py`).
2. Enter the initial number of coins you want to start the game with.
3. Take turns with the computer player to grab coins, following the rules mentioned above.
4. The game continues until there are no more coins left.
5. The player who takes the last coin loses the game.

## Code Structure

The code is organized into the following functions:

- **player_takes_coins():**
  - Handles human player input for the number of coins to take.
  - Ensures the input is valid (between 1 and 3).

- **computer_takes_coins(coins):**
  - Implements a simple algorithm for the computer player to make a strategic move.
  - Chooses a random number of coins to take if the algorithm doesn't provide a specific value.

- **coin_game(coins):**
  - Manages the overall flow of the game, alternating between human and computer player turns.
  - Prints the current state of the game and updates the number of coins.

- **main():**
  - Provides an introduction to the game and prompts the user to input the initial number of coins.
  - Calls the coin_game function to start the game.

## Getting Started

1. Ensure you have Python installed on your system.
2. Download the "coin_grab_game.py" file.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script using the command `python coin_grab_game.py`.
5. Follow the on-screen instructions to play the game.

Enjoy playing "Coin Grab" and challenge yourself to outsmart the computer player!
