"""Tic Tac Toe Game"""

import numpy as np
import sys
from functools import cache


class tic_tac_toe:
    def __init__(self):
        self.board = np.array([["", "", ""], ["", "", ""], ["", "", ""]])

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

        self.player_maps = {"Player": "X", "Computer": "O"}
        self.players = list(self.player_maps.keys())
        self.symbols = self.player_maps.values()
        self.player_turn = np.random.choice(self.players)

    def change_player(self):
        if self.player_turn == self.players[0]:
            self.player_turn = self.players[1]
        else:
            self.player_turn = self.players[0]

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

    def create_check_arrays(self):
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
        return check_these

    def isTie(self):
        if "" not in self.board:
            return True
        else:
            return False

    def check_game_over(self):
        arr_tb_check = self.create_check_arrays()
        if len(arr_tb_check) > 0:
            for i in arr_tb_check:
                if self.check_repeating_letter(i):
                    return True
            if self.isTie():
                return True
        return False

    # will only work if game is over
    def winning_player(self):
        arr_tb_check2 = self.create_check_arrays()
        for i in arr_tb_check2:
            if self.check_repeating_letter(i):
                if np.unique(i)[0] == self.player_maps["Computer"]:
                    return "Computer"
                elif np.unique(i)[0] == self.player_maps["Player"]:
                    return "Player"
                else:
                    pass
        if self.isTie():
            return "Tie"

    def minimax(self, Comp_turn):

        if self.check_game_over():
            if self.winning_player() == "Computer":
                return 1
            elif self.winning_player() == "Player":
                return -1
            elif self.winning_player() == "Tie":
                return 0
            else:
                pass
        else:

            if Comp_turn:
                scores = []
                place = []
                for i, j in enumerate(self.board.flatten()):
                    if j == "":

                        self.board[self.place_maps[i + 1]] = self.player_maps[
                            "Computer"
                        ]
                        place.append(i + 1)
                        scores.append(self.minimax(False))

                        self.board[self.place_maps[i + 1]] = ""
                return max(scores)
            else:
                place = []
                scores = []
                for i, j in enumerate(self.board.flatten()):
                    if j == "":
                        self.board[self.place_maps[i + 1]] = self.player_maps["Player"]
                        place.append(i + 1)
                        scores.append(self.minimax(True))
                        self.board[self.place_maps[i + 1]] = ""
                return min(scores)

    def computer_play(self):
        place = []
        score = []
        for i, j in enumerate(self.board.flatten()):
            if j == "":

                self.board[self.place_maps[i + 1]] = self.player_maps["Computer"]
                place.append(i + 1)
                score.append(self.minimax(False))

                self.board[self.place_maps[i + 1]] = ""
        return place[np.argmax(score)]

    def turn(self, ok=True):

        while self.check_game_over() == False:
            if self.player_turn == "Computer":
                self.board[self.place_maps[self.computer_play()]] = self.player_maps[
                    "Computer"
                ]
                print(self.board)
                if self.check_game_over():
                    break
                self.change_player()

            if self.player_turn == "Player":

                print("Your Turn")
                place = int(input("please enter the position"))
                if self.board[self.place_maps[place]] != "":
                    print("place occupied, Please Try again")
                    self.turn()
                else:
                    self.board[self.place_maps[place]] = self.player_maps["Player"]
                    print(self.board)
                    ok = True
                    self.change_player()
