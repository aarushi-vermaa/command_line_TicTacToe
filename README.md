[![GitHub license](https://img.shields.io/github/license/aarushi-vermaa/Biostat821_Final_Project)](https://github.com/aarushi-vermaa/Biostat821_Final_Project/blob/main/LICENSE)

# Lets play Tic-Tac-Toe

Welcome to the TickTacToe game. This repository is for the Final Project for BIOSTATS821 course - Software Tools for Data Science at Duke University.
We are building a Tic-Tac-Toe game using Python. The user can play against another user or against the computer using the command line prompt.

## How to Play

### The Board

```text
[['', '', ''],

  ['', '', ''],
  
  ['', '', '']]
```

The board is a 3x3 grid as represented above. The first player will always have an X mark, and the second player will always have an O mark. Each player can place their mark during their respective turns by entering the number corresponding to the position they want to place the mark on. Please refer to the grid below to see which number corresponds to which place on the grid.

```text
[[ 1,  2, 3],

  [4, 5, 6],
  
  [7, 8, 9]]
```

For example, if a user wants to play their turn in the top right corner, they enter the number 3 into the command prompt and their corresponding mark will be placed there. If the position on the grid is already occupied, an `INVALID MOVE` error will appear and the player will be asked to select again.  Throughout the game, if the player types an input that is not acceptable, an `INVALID INPUT` error will appear and the player will be shown what the acceptable inputs are and they will be asked to try again.

### Players Selection

When the game is loaded, the user needs to select the players. The user can choose to play against another player or against the computer.
When the game begings, the user is prompted to choose between the two. By entering the appropriate option (1 for Player vs. Player and 2 for Player vs. Computer). The player who plays first is selected randomly.

### Player versus Player

If two human players are playing, the command prompt will display which Player's turn it is. To play their turn, each corresponding user must specify the position to be played on the 3x3 grid. The inputs range between the number 1-9 as displayed in the grid in The Board section.

### Player versus Computer

If the user is playing against the computer, the command prompt will display if it is the Computer's turn or the User's turn. To play their turn, the user must specify the position to be played on the 3x3 grid. After that the computer will perform its move.

### Game Over

Once the game has a winner or there is a tie, the prompt will display the outcome of the game.
From here the user can choose to either quit the game or start a new game by answering the prompt,
`Do you want to play again? (Answer Y/N)`

----

## Getting up and running

This project is built with Python 3. In order to play the game, please follow the following steps:

Step 1: Git clone the repo on your local machine

```text
git clone https://github.com/aarushi-vermaa/Biostat821_Final_Project.git
```

This will clone all the files on Github to your local machine

Step 2: Install required packages

```text
pip install -r requirements.txt
```

Running this command will install the packages used to build the game. This will allow you to play the game seamlessly

Step 3: Run the game on your local machine

```python
python3 TicTacToe_no_cache.py
```

Running this command will beging the game. Follow the instructions displayed to play the game.

We hope you enjoy the game!

## Testing

To test the functions in the game:

```python
pytest test_ttt.py -s
```

To test the coverage of the tests:

```python
pytest test_ttt.py -s -cov
```

----

### Authors

[Mohammad Anas](https://github.com/anas14680), [Sydney Donati-Leach](https://github.com/sdonatileach), [Aarushi Verma](https://github.com/aarushi-vermaa)
