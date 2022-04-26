"""Tic Tac Toe Game"""

import numpy as np
import sys
from functools import cache


class tic_tac_toe:
    """CLass tic tac toe."""

    def __init__(self) -> None:
        """Constructor for class tic tac toe."""
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

        self.game_mode = input(
            "Do you want to against the computer or another player?\
(Answer: Computer/Another Player):  "
        )
        # keep asking until user gives the a desired anwer without throwing an error
        while self.game_mode not in ["Computer", "Another Player"]:
            print("Please respond with either 'Computer' or 'Another Player'")
            self.game_mode = input(
                "Do you want to against the computer or another player?\
(Answer: Computer/Another Player):  "
            )

        # create game players in accordance with the game mode
        # the functions below (in our class) are written in a way to automatically
        # take care of the game.mode and the players in it.
        # Point being that we do not have to use too many if-else
        # statements to write code for each game mode and each player
        # in the game mode
        if self.game_mode == "Computer":
            # if you change the name here for the Computer and
            # the user make sure to change these names in the minimax
            # function (Will comment out there as well)
            self.player_maps = {"User": "X", "Computer": "O"}
        else:
            self.player_maps = {"Player 1": "X", "Player 2": "O"}

        # self.players depends on the self.player maps
        self.players = list(self.player_maps.keys())
        self.player_turn = np.random.choice(self.players)
        self.turns_played = 0
        self.score_board = {self.players[0]: 0, self.players[1]: 0, "Ties": 0}

    # during the game we ask users serveral questions
    # like which move to play. If user accidentaly answers some
    # thing wrong the game will throw an error and will need
    # to be restarted. to avoid that we create this method.
    def ask_question(self, input_string: str, desired_answers: list[str]) -> str:
        """Ask user the question and keep asking until answered correctly."""
        answer = input(input_string)
        while answer not in desired_answers:
            print("Please respond with on of the following:", desired_answers)
            answer = input(input_string)
        return answer

    def change_player(self) -> None:
        """Change the game player who is taking turn."""
        # will change to the other player playing
        # regardless of game mode
        if self.player_turn == self.players[0]:
            self.player_turn = self.players[1]
        else:
            self.player_turn = self.players[0]

    def check_repeating_letter(self, a: np.ndarray) -> bool:
        """Check if an array has all the same shapes."""
        flag = True
        for i in range(1, len(a)):
            if a[i] != a[i - 1]:
                flag = False
                return flag
        return flag

    def diagonal(self) -> tuple[np.ndarray, np.ndarray]:
        """Create the two diaganols of the board."""
        diagonal1: list[str] = []
        diagonal2: list[str] = []
        for i in range(3):
            for j in range(3):
                if i == j:
                    diagonal1.append(self.board[i, j])
                    diagonal_1 = np.array(diagonal1)
                if i + j == 2:
                    diagonal2.append(self.board[i, j])
                    diagonal_2 = np.array(diagonal2)
        return diagonal_1, diagonal_2

    def create_check_arrays(self) -> list[np.ndarray]:
        """Create arrays that need to be checked to determine if the game is over."""
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

    def isTie(self) -> bool:
        """Check if its a tie."""
        if "" not in self.board:
            return True
        else:
            return False

    def check_game_over(self) -> bool:
        """Check if the game is over."""
        arr_tb_check: np.ndarray = self.create_check_arrays()
        if len(arr_tb_check) > 0:
            for i in arr_tb_check:
                if self.check_repeating_letter(i):
                    return True
            if self.isTie():
                return True
        return False

    # will only work if game is over
    def winning_player(self) -> str:
        """Return the winning player."""
        arr_tb_check2: np.ndarray = self.create_check_arrays()
        for i in arr_tb_check2:
            if self.check_repeating_letter(i):
                if np.unique(i)[0] == self.player_maps[self.players[0]]:
                    return self.players[0]
                elif np.unique(i)[0] == self.player_maps[self.players[1]]:
                    return self.players[1]
                else:
                    pass
        if self.isTie():
            return "Tie"

    # a recursive function
    # aims to maximie computer rewards but also assumes that the user will always play the optimal move.
    # Computer will play its best move. Then the computer puts itself in users place
    # and place the best move from user's perspective.
    # Then the computer plays its own best move again
    # The Comp_turn is bool arguement that indicates if the computer is playing
    # from a user perspective or a computer perspective.

    def minimax(self, Comp_turn: bool) -> int:
        """Impliment minimax."""

        # we define rewards for the computer
        # these rewards are maximised by computer
        # while minimized by user
        # then we make the terminal state
        # this is when one hypothetical scenario of the played out gam ends

        # if the game players name are changes in self.player_maps
        # please change them here as well
        if self.check_game_over():
            if self.winning_player() == "Computer":
                return 1
            elif self.winning_player() == "User":
                return -1
            elif self.winning_player() == "Tie":
                return 0
            else:
                pass
        else:
            # checks if its computer turn or not
            if Comp_turn:
                # if it is computers turn it will play the move below
                scores = []
                # go over each available move
                for i, j in enumerate(self.board.flatten()):
                    if j == "":
                        # if the game players name are changes in self.player_maps
                        # please change them here as well
                        # play that move
                        self.board[self.place_maps[i + 1]] = self.player_maps[
                            "Computer"
                        ]
                        # now that computer has played its move
                        # we call minimax again to but with comp_turn as False
                        # so computer plays from a users perpective
                        ans = self.minimax(False)
                        scores.append(ans)
                        # undo the move as the next time the computer is experimenting
                        # with different moves. If we do not undo all the previous hypothetical moves
                        # played will be retained in the board.
                        self.board[self.place_maps[i + 1]] = ""
                # scores are maximized as the computer is playing that move
                return max(scores)

            else:
                # if computer plays from a user perspective then the following is done
                # all literally the same
                # plays every possible move from user perspective
                scores = []
                for i, j in enumerate(self.board.flatten()):
                    if j == "":
                        # if the game players name are changes in self.player_maps
                        # please change them here as well
                        self.board[self.place_maps[i + 1]] = self.player_maps["User"]

                        # once move is played the minimax below with comp-turn true is called
                        # so the computer than plays its move from its own perspective
                        ans = self.minimax(True)
                        scores.append(ans)
                        # undo the move
                        self.board[self.place_maps[i + 1]] = ""
                # as the move is played by the computer from a users perspective
                # and the fact that user wants to minimize computer scores here
                # we write computers move
                return min(scores)

    def computer_play(self) -> int:
        """Plays the computer move."""
        # Minimax function above only keeps track of the scores at each position
        # here we keep track of scores and move to be played.
        # It is the optimal move we want
        # Given the current state if the board, the computer plays each possible move
        # then calls the minimax on board that incorporates that move
        # keeps track of the scores achived on that move
        move = []
        score = []
        for i, j in enumerate(self.board.flatten()):
            if j == "":

                self.board[self.place_maps[i + 1]] = self.player_maps["Computer"]
                move.append(i + 1)
                score.append(self.minimax(False))

                self.board[self.place_maps[i + 1]] = ""
        # returns the best move
        return move[np.argmax(score)]

    def game(self):
        """Plays an episode of the game till the end."""
        print(self.board)
        while self.check_game_over() == False:
            # played if game.mode is One Player
            # in that case the chunk of code below will
            # play the computers move
            if self.player_turn == "Computer":
                print("Computer's Turn")
                # hardcoded part for if computer plays the first turn
                if self.turns_played == 0:
                    self.board[0, 0] = self.player_maps["Computer"]
                else:
                    self.board[
                        self.place_maps[self.computer_play()]
                    ] = self.player_maps["Computer"]
                print(self.board)
                if self.check_game_over():
                    break
                self.turns_played += 1
                self.change_player()

            else:
                # the code plays the players move
                # if game.mode is One Player
                # it will play the users move
                # if the game.mode is two players
                # it will play the move of each player
                # one by one
                print(f"{self.player_turn}'s Turn")
                potential_moves = [str(i) for i in self.place_maps.keys()]
                move = self.ask_question(
                    "Please enter the position you want to play:  ", potential_moves
                )

                if self.board[self.place_maps[int(move)]] != "":
                    print("Position occupied, Please Try again")
                    self.game()
                else:
                    self.board[self.place_maps[int(move)]] = self.player_maps[
                        self.player_turn
                    ]

                    print(self.board)
                    self.turns_played += 1
                    self.change_player()

        # now that the game is over we check who wins
        # and add points to the score board accordingly
        if self.winning_player() == "Tie":
            print("Its a Tie")
            self.score_board["Ties"] += 1
        elif self.winning_player() == self.players[0]:
            print(f"{self.players[0]} Won.")
            self.score_board[self.players[0]] += 1
        elif self.winning_player() == self.players[1]:
            print(f"{self.players[1]} Won.")
            self.score_board[self.players[1]] += 1

        # asks if the game need to be played again.
        self.play_again()

    def reset_game(self) -> None:
        """This will reset the game"""
        self.player_turn = np.random.choice(self.players)
        self.turns_played = 0
        self.board = np.array([["", "", ""], ["", "", ""], ["", "", ""]])

    def play_again(self) -> None:
        """Something similar to what Sydney did."""

        # ask if wants to play again
        game_again = self.ask_question(
            "Do you want to play again? Answer (yes/no):  ", ["yes", "no"]
        )

        # after each episode of the game the score board is displayed
        print("Total games Played:", sum(self.score_board.values()))
        print(f"{self.players[0]} has won {self.score_board[self.players[0]]} games.")
        print(f"{self.players[1]} has won {self.score_board[self.players[1]]} games.")
        print(f"{self.score_board['Ties']} games have resulted in a tie.")

        if game_again == "no":
            # if no more games to be played print the player who won the most games
            if self.score_board[self.players[0]] > self.score_board[self.players[1]]:
                print(self.players[0], " won majority games.")
            elif self.score_board[self.players[0]] < self.score_board[self.players[1]]:
                print(self.players[0], " won majority games.")
            else:
                print(
                    self.players[0],
                    " and ",
                    self.players[1],
                    " won equal number of games.",
                )
            # print a farewell line
            print(
                "Hope you enjoyed playing Tic Tac Toe. \
Add a nice farewell here if needed or remove this line."
            )
        # if more game to be played than reset the game and play on
        else:
            self.reset_game()
            self.game()


if __name__ == "__main__":
    game = tic_tac_toe()
    game.game()
