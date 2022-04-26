"""Tic Tac Toe Game"""

import numpy as np
import sys
from typing import List, Dict, Tuple, Union


class tic_tac_toe:
    """Tic Tac Toe Class."""

    def __init__(self) -> None:
        """Initiate Class."""
        # Creating the board using 3 empty arrays
        self.board = np.array([["", "", ""], ["", "", ""], ["", "", ""]])

        # Keys in the dictionary represent the position on the board
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

        # The keys sepcify keys are comp_turn argument
        # values are list of list
        # the first list is list of board states
        # the second list corresponds to the
        # minimax for the board states in the
        # first list
        self.minimax_cache: Dict[bool, List[Union[List[np.ndarray], List[str]]]] = {
            False: [[], []],
            True: [[], []],
        }

        self.game_mode = input(
            "Welcome to Tic Tac Toe!\n Enter '1' for Player vs Player, '2' for Player vs Computer: "
        )
        # The question is repeated until user submits the acceptable answer
        while self.game_mode not in ["1", "2"]:
            print("INVALID INPUT: Please respond with either '1' or '2'")
            self.game_mode = input(
                "Enter '1' for Player vs Player, '2' for Player vs Computer: "
            )

        # Create the Players of the game on the basis of User's input
        if self.game_mode == "2":
            self.player_maps = {"User": "X", "Computer": "O"}
        else:
            self.player_maps = {"Player 1": "X", "Player 2": "O"}

        self.players = list(self.player_maps.keys())
        self.player_turn = np.random.choice(self.players)
        self.turns_played = 0
        self.score_board = {self.players[0]: 0, self.players[1]: 0, "Ties": 0}

    def ask_question(self, input_string: str, desired_answers: List[str]) -> str:
        """Ask user the question and repeat question till user inputs acceptable answer.

        The user is asked for inputs multiple times during the game. We create this
        helper function to repeat the question if the user accidentaly answers something wrong.
        Otherwise, the game would end prematurely and the user would have to start over."""

        answer = input(input_string)
        while answer not in desired_answers:
            print(
                "INVALID INPUT. Please respond with one of the following: ",
                desired_answers,
            )
            answer = input(input_string)
        return answer

    def swap_player(self) -> None:
        """Swaps the player's turns."""
        if self.player_turn == self.players[0]:
            self.player_turn = self.players[1]
        else:
            self.player_turn = self.players[0]

    #####################################################
    ### To think of better function name
    def check_repeating_letter(self, a: np.ndarray) -> bool:
        """Check if an array has all the same letter."""
        flag = True
        for i in range(1, len(a)):
            if a[i] != a[i - 1]:
                flag = False
                return flag
        return flag

    def diagonal(self) -> Tuple[np.ndarray, np.ndarray]:
        """Create arrays that represent the two diagonals on the board."""
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

    def create_check_arrays(self) -> List[np.ndarray]:
        """Create arrays that need to be checked to determine if the game is over"""
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

    def is_tie(self) -> bool:
        """Check if the game has ended in a tie."""
        if "" not in self.board:
            return True
        else:
            return False

    def check_game_over(self) -> bool:
        """Check if the game is over."""
        arr_tb_check = self.create_check_arrays()
        if len(arr_tb_check) > 0:
            for i in arr_tb_check:
                if self.check_repeating_letter(i):
                    if self.winning_player() == self.players[0]:
                        print(f"{self.players[0]} Won!\n")
                        self.score_board[self.players[0]] += 1
                    elif self.winning_player() == self.players[1]:
                        print(f"{self.players[1]} Won!\n")
                        self.score_board[self.players[1]] += 1
                    return True
            if self.is_tie():
                print("It's a Tie!\n")
                self.score_board["Ties"] += 1
                return True
        return False

    def winning_player(self) -> str:
        """Return the winning player if the game has ended."""
        arr_tb_check2 = self.create_check_arrays()
        if self.is_tie():
            return "Tie"
        else:
            for i in arr_tb_check2:
                if self.check_repeating_letter(i):
                    if np.unique(i)[0] == self.player_maps[self.players[0]]:
                        return self.players[0]
                    elif np.unique(i)[0] == self.player_maps[self.players[1]]:
                        return self.players[1]

    #################################
    ## To think of a better name for this function ##
    def check_in_cache(
        self, board_state: np.ndarray, Comp_turn: bool
    ) -> Union[int, str]:
        """Check if minimax for a particular board state for a
        Comp_turn has been calculated. If yes return the minimax value.
        Else return Not found."""
        for i in range(len(self.minimax_cache[Comp_turn][0])):
            if np.array_equiv(self.minimax_cache[Comp_turn][0][i], board_state):
                return self.minimax_cache[Comp_turn][1][i]
        return "Not found"

    def minimax(self, Comp_turn: bool) -> Union[int, str]:
        """A recursive function that aims to maximize computer rewards.
        Then the computer puts itself in users place
        and places the best move from user's perspective.
        Then the computer plays its own best move again
        The Comp_turn is bool argument that indicates if the computer is playing
        from a user perspective or a computer perspective."""
        # if minimax for board state stored in cache
        # return its value else compute minimax
        if self.check_in_cache(self.board, Comp_turn) in [-1, 0, 1]:
            return self.check_in_cache(self.board, Comp_turn)
        else:
            # we define rewards for the computer
            # these rewards are maximized by computer
            # while minimized by user
            # if self.check_game_over():
            if self.winning_player() == "Computer":
                return 1
            elif self.winning_player() == "User":
                return -1
            elif self.winning_player() == "Tie":
                return 0
            else:
                # checks if its computer turn or not
                if Comp_turn:
                    # if it is computers turn it will play the move below
                    scores = []
                    # go over each available move
                    for i, j in enumerate(self.board.flatten()):
                        if j == "":
                            # play that move
                            self.board[self.place_maps[i + 1]] = self.player_maps[
                                "Computer"
                            ]
                            # now that computer has played its move
                            # we call minimax again but with comp_turn as False
                            # so computer plays from a users perpective
                            ans = self.minimax(False)
                            # Add minimax value for the board state to cache
                            self.minimax_cache[False][0].append(self.board.copy())
                            self.minimax_cache[False][1].append(ans)
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
                            self.board[self.place_maps[i + 1]] = self.player_maps[
                                "User"
                            ]
                            # once move is played the minimax below with comp-turn true is called
                            # so the computer than plays its move from its own perspective
                            ans = self.minimax(True)
                            # add minimax value for board state to cache
                            self.minimax_cache[True][0].append(self.board.copy())
                            self.minimax_cache[True][1].append(ans)
                            scores.append(ans)

                            # undo the move
                            self.board[self.place_maps[i + 1]] = ""
                    # as the move is played by the computer from a users perspective
                    # and the fact that user wants to minimize computer scores here
                    # we write computers move
                    return min(scores)

    def computer_play(self) -> int:
        """Plays the computer move.
        Minimax function above only keeps track of the scores at each position
        here we keep track of scores and move to be played.
        It is the optimal move we want
        Given the current state if the board, the computer plays each possible move
        then calls the minimax on board that incorporates that move
        keeps track of the scores achived on that move"""
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
        """Plays one instance of the game until the game ends."""
        while self.check_game_over() == False:
            # check if its the computer's turn
            if self.player_turn == "Computer":
                print("\nComputer's Turn")
                # hardcoded part for if computer plays the first turn
                if self.turns_played == 0:
                    self.board[0, 0] = self.player_maps["Computer"]
                elif self.turns_played == 1:
                    # if computer takes second turn, cache memoization takes about 30 seconds
                    # print something so the user knows it's thinking
                    print("Computer is thinking...")
                    self.board[
                        self.place_maps[self.computer_play()]
                    ] = self.player_maps["Computer"]
                else:
                    self.board[
                        self.place_maps[self.computer_play()]
                    ] = self.player_maps["Computer"]
                print(self.board)
                self.turns_played += 1
                self.swap_player()
            # otherwise it's a user's turn in either a one-player or two-player game
            else:
                print(f"\n{self.player_turn}'s Turn")
                potential_moves = [str(i) for i in self.place_maps.keys()]
                move = self.ask_question(
                    "Please enter the position you want to play:  ", potential_moves
                )

                if self.board[self.place_maps[int(move)]] == "":
                    # place either an X or an O on the board where the user wants to play
                    # this is pulled from the player_maps dictionary that defines the letter to be played
                    # depending on whose turn it is
                    self.board[self.place_maps[int(move)]] = self.player_maps[
                        self.player_turn
                    ]

                    print(self.board)
                    self.turns_played += 1
                    self.swap_player()

                else:
                    print("INVALID MOVE. Position occupied. Please try again.")

        self.play_again()

    def reset_game(self) -> None:
        """This function reset the game to an empty board. Players can start playing again."""
        self.player_turn = np.random.choice(self.players)
        self.turns_played = 0
        self.board = np.array([["", "", ""], ["", "", ""], ["", "", ""]])

    def play_again(self) -> None:
        """Asks user if they want to play again or quit the game."""

        # ask if wants to play again
        game_again = self.ask_question(
            "Do you want to play again? (Answer Y/N): ", ["Y", "N"]
        )
        player0wins = self.score_board[self.players[0]]
        player1wins = self.score_board[self.players[1]]
        totalgames = sum(self.score_board.values())

        print("\nTotal games Played:", totalgames)
        print(f"{self.players[0]} win count: {player0wins}")
        print(f"{self.players[1]} win count: {player1wins}")
        print(f"Ties: {self.score_board['Ties']}")

        if game_again == "N":
            # if no more games to be played print the player who won the most games
            if player0wins > player1wins:
                print(
                    f"\n{self.players[0]} won {player0wins} out of {totalgames} game(s). They are the winner!\n"
                )
            elif player0wins < player1wins:
                print(
                    f"\n{self.players[1]} won {player1wins} out of {totalgames} game(s). They are the winner!\n"
                )
            else:
                print(
                    f"\n{self.players[0]} and {self.players[1]} won equal number of games.\n"
                )
            # print a farewell line
            print("Hope you enjoyed playing Tic Tac Toe. See you next time. Bye!")
        # if more game to be played than reset the game and play on
        else:
            self.reset_game()
            self.game()


if __name__ == "__main__":
    game = tic_tac_toe()
    game.game()