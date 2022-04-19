"""Tic Tac Toe Game"""
import numpy as np
import warnings

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

    def check_one(self, a):
        flag = True
        for i in range(1, len(a)):
            if a[i] != a[i - 1]:
                flag = False
                return flag
        return flag

    def check_game_over(self):
        check_these = []
        for i in range(3):
            if ("O" in self.board[:, i]) or ("X" in self.board[:, i]):
                check_these.append(self.board[:, i])
            elif ("O" in self.board[i, :]) or ("X" in self.board[i, :]):
                check_these.append(self.board[i, :])

        diagonal1 = np.array([])
        diagonal2 = np.array([])
        for i in range(3):
            for j in range(3):
                if i == j:
                    np.append(diagonal1, board[i, j])
                elif i + j == 2:
                    np.append(diagonal2, board[i, j])
        if ("O" in list(diagonal1)) or ("X" in list(diagonal1)):
            check_these.append(diagonal1)
        if ("O" in diagonal2) or ("X" in diagonal2):
            check_these.append(diagonal2)

        if len(check_these) > 0:
            for i in check_these:

                if self.check_one(i):
                    print("Game Over")
                    element = np.unique(i)[0]
                    rev_players = dict(zip(self.players.values(), self.players.keys()))
                    print(f"{rev_players[element]} Wins!")
                    return True
        return False

    def turn(self):
        while self.check_game_over() == False:
            print(f"{self.player_turn}'s Turn.")
            place = input(f"{self.players} Please enter the position:")
            board_place = self.place_maps[int(place)]
            if self.board[board_place] == "":
                self.board[board_place] = self.players[self.player_turn]
            else:
                print("Position Occupied. Please Try Again.")
                self.turn()

            if self.player_turn == "Player 1":
                self.player_turn = "Player 2"
            elif self.player_turn == "Player 2":
                self.player_turn = "Player 1"

            if "" not in self.board:
                print("Its a Tie.")
                break

            print(self.board)
