
# Tic-Tac-Toe Game

This is a simple implementation of the classic Tic-Tac-Toe game. It can be played between two players on the same machine. The game will check for a winner after each move and declare the winner if there is one. If all positions are filled and there is no winner, it will declare the game as a draw.

## Features
- Two-player gameplay
- Checks for winner after every move
- Declares draw if all positions are filled without a winner
- User-friendly console interface

## How to Run

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/janisadhi/Tic-Tac-Toe.git
   cd Tic-Tac-Toe
   ```

2. Create a virtual environment.

   On macOS/Linux:

   ```bash
   python3 -m venv venv
   ```

   On Windows:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment.

   On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

4. Install the required dependencies from the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

5. Run the game using the following command:

   ```bash
   python app.py
   ```

6. Follow the on-screen prompts to play the game.

## How to Play

- The game is played by two players. Player 1 uses `X`, and Player 2 uses `O`.
- Players take turns to place their mark on the 3x3 grid.
- The first player to align three marks in a row (vertically, horizontally, or diagonally) wins.
- If all positions are filled and no one wins, the game will declare a draw.

## Example Gameplay

```
Player 1 (X) - Choose a position between 1-9: 1
Player 2 (O) - Choose a position between 1-9: 5
Player 1 (X) - Choose a position between 1-9: 9
Player 2 (O) - Choose a position between 1-9: 3

... and so on.

Player 1 wins!
```

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`

