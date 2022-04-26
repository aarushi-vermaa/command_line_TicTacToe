"""Test Tic Tac Toe classes and functions."""
import tictactoe_game as ttt
import numpy as np

# Initialize class for testing
game = ttt.TicTacToe()


def test_game_board():
    """Test Tic Tac Toe.

    This function tests if the board is created correctly.
    """
    assert game.board.shape == (3, 3)
    assert np.array_equiv(
        game.board, np.array([["", "", ""], ["", "", ""], ["", "", ""]])
    )


def test_ask_question(monkeypatch):
    """Test the ask_question function.

    This function tests if the ask question function
    correctly accepts a correct input entered by the user.
    """
    # This simulates the user entering "1" in the terminal:
    inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for response in inputs:
        monkeypatch.setattr("builtins.input", lambda _: response)
        # go about using input() like you normally would:
        a = game.ask_question(response, [str(i) for i in game.place_maps.keys()])
        assert a == response


def test_check_repeating_letter():
    """Test the check_repeating_letter function.

    This function tests if an array has 3 of the same
     letters the check_repeating letter function returns True,
     else False.
    """
    assert game.check_repeating_letter(np.array(["X", "X", ""])) == False
    assert game.check_repeating_letter(np.array(["X", "X", "X"])) == True


def test_check_game_over():
    """Test the check_game_over function.

    This function tests if the check_game_over function correctly identifies
    a game is over or not. It returns True when game is over else False.
    """
    game.board = np.array([["X", "X", "X"], ["", "", ""], ["", "", ""]])
    assert game.check_game_over() == True
    game.board = np.array([["X", "", "X"], ["", "O", "O"], ["X", "", ""]])
    assert game.check_game_over() == False
    game.board = np.array([["X", "", ""], ["X", "O", "O"], ["X", "", ""]])
    assert game.check_game_over() == True
    game.board = np.array([["X", "O", "X"], ["X", "O", "X"], ["O", "X", "O"]])
    assert game.check_game_over() == True


def test_winning_player():
    """Test the winning player function.

    This functions tests whether the correct winning player is returned
    based on the winning mark or if the game has ended in a Tie.
    """
    if game.game_mode == "1":
        game.board = np.array([["X", "O", "O"], ["X", "O", "X"], ["O", "X", "O"]])
        assert game.winning_player() == "Player 2"

        game.board = np.array([["X", "", ""], ["X", "O", "O"], ["X", "", ""]])
        assert game.winning_player() == "Player 1"

        game.board = np.array([["X", "O", "X"], ["X", "O", "X"], ["O", "X", "O"]])
        assert game.winning_player() == "Tie"
    else:
        game.board = np.array([["X", "O", "O"], ["X", "O", "X"], ["O", "X", "O"]])
        assert game.winning_player() == "Computer"

        game.board = np.array([["X", "", ""], ["X", "O", "O"], ["X", "", ""]])
        assert game.winning_player() == "User"

        game.board = np.array([["X", "O", "X"], ["X", "O", "X"], ["O", "X", "O"]])
        assert game.winning_player() == "Tie"


def test_computer_play():
    """Test the 31 lines of code dedicated to the computer's play.

    This function tests multiple functions when the user is playing
    against the Computer. It checks if the correct move is returned
    based on the highest score calculated using the minimax function.
    """
    if game.game_mode == "2":
        game.board = np.array([["O", "X", "X"], ["", "X", ""], ["", "O", "O"]])
        assert game.computer_play() == 7
    else:
        pass
