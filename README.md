# Lets play Tic-Tac-Toe

Welcome to the TickTacToe game. This repository is for the Final Project for BIOSTATS821 course - Software Tools for Data Science at Duke Univeristy.
We are building a Tic-Tac-Toe game using Python. The user can play against another user or against the computer using the command prompt.

## How to Play

### The Board

```text
[['', '', ''],

  ['', '', ''],
  
  ['', '', '']]
```

The board is a 3x3 grid as represented above. Each player can place their mark (either X or O) during their respective turns by entering the number corresponding to the position they want to place the Mark on. Please refer to the grid below to see which cumber corresponds to which place on the grid.

```text
[[ 1,  2, 3],

  [4, 5, 6],
  
  [7, 8, 9]]
  
```

For example, if a user wants to play their turn in top right corner, they enter the number 3 into the command prompt and their corresponding mark will be placed there.

### Players Selection

When the game is loaded, you need to select your players. You need to select the type of player you want by **(to be updated)** , either computer or human. The player who goes first is selected randomly.

### Human versus Human

If two human players are playing, the command prompt will display which Player's turn it is. To play your turn, you must specify the position to be played on the 3x3 grid.

### Human versus Computer

If you are playing against the computer, the command prompt will display which Player's turn it is. To play your turn, you must specify the position to be played on the 3x3 grid, after that the computer will perform its move.

### Game Over

Once the game has a winner or there is a draw, you will see prompt stating the outcome. From here you can start a new game by **(to update how)**

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

Step 3: **To update**

----

### Authors

[Mohammad Anas](https://github.com/anas14680), [Sydney Donati-Leach](https://github.com/sdonatileach), [Aarushi Verma](https://github.com/aarushi-vermaa)
