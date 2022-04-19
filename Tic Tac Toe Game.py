"""Tic Tac Toe Game"""
import numpy as np
import warnings
import sys

warnings.filterwarnings("ignore")


class tic_tac_toe:
    def __init__(self):
        self.board = np.array([["", "", ""], ["", "", ""], ["", "", ""]])
        self.players = {"Player 1": "O", "Player 2": "X"}
        self.place_maps = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2),
        }
        self.player_turn = np.random.choice(list(self.players.keys()), 1, [0.5, 0.5])[0]
        return self.turn()

    def check_repeating_letter(self, a):
        flag = True
        for i in range(1, len(a)):
            if a[i] != a[i - 1]:
                flag = False
                return flag
        return flag

    def diagonal(self):
        diagonal1 = []
        diagonal2 = []
        for i in range(3):
            for j in range(3):
                if i == j:
                    diagonal1.append(self.board[i, j])
                    diagonal_1 = np.array(diagonal1)
                if i + j == 2:
                    diagonal2.append(self.board[i, j])
                    diagonal_2 = np.array(diagonal2)
        return diagonal_1, diagonal_2

    def check_game_over(self):
        check_these = []
        for i in range(3):
            if ("O" in self.board[:, i]) or ("X" in self.board[:, i]):
                check_these.append(self.board[:, i])
            if ("O" in self.board[i, :]) or ("X" in self.board[i, :]):
                check_these.append(self.board[i, :])
        diagonal_1, diagonal_2 = self.diagonal()
        if ("O" in list(diagonal_1)) or ("X" in list(diagonal_1)):
            check_these.append(diagonal_1)
        if ("O" in list(diagonal_2)) or ("X" in list(diagonal_2)):
            check_these.append(diagonal_2)

        if len(check_these) > 0:
            for i in check_these:

                if self.check_repeating_letter(i):
                    print("Game Over")
                    element = np.unique(i)[0]
                    rev_players = dict(zip(self.players.values(), self.players.keys()))
                    print(f"{rev_players[element]} Wins!")
                    return True

                elif "" not in self.board:
                    print("It's a Tie!")
                    return True
        return False

    def turn(self):
        while self.check_game_over() == False:
            print(f"{self.player_turn}'s Turn.")
            place = input(f"{self.players} Please enter the position:")
            if place.isdigit():
                if int(place) in self.place_maps.keys():
                    board_place = self.place_maps[int(place)]
                else:
                    print("Invalid input. Please enter a number between 1 and 9.")
                    self.turn()
            else:
                print("Invalid input. Please enter a number between 1 and 9")
                self.turn()
            if self.board[board_place] == "":
                self.board[board_place] = self.players[self.player_turn]
            else:
                print("Position Occupied. Please Try Again.")
                self.turn()
            if self.player_turn == "Player 1":
                self.player_turn = "Player 2"
            elif self.player_turn == "Player 2":
                self.player_turn = "Player 1"

            print(self.board)
