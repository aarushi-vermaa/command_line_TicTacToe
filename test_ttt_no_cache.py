"""Test Tic Tac Toe classes and functions."""
import pytest
import TicTacToe_no_cache as ttt
import numpy as np

game = ttt.tic_tac_toe()

def test_game_board():
    """Test Tic Tac Toe."""
    assert game.board.shape == (3,3)
    assert np.array_equiv(game.board, \
        np.array([["", "", ""], ["", "", ""], ["", "", ""]]))

def test_ask_question(monkeypatch):
    """Test the ask_question function."""
    # This simulates the user entering "1" in the terminal:
    inputs = (['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    for response in inputs:
        monkeypatch.setattr('builtins.input', lambda _: response)
        # go about using input() like you normally would:
        a = game.ask_question(response, \
        [str(i) for i in game.place_maps.keys()])
        assert a == response
    
# def test_invalid_input(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda _: "INVALID INPUT. Please respond with one of the following: ")
#     # go about using input() like you normally would:
#     b = game.ask_question("b", \
#         [str(i) for i in game.place_maps.keys()])
#     assert b == "INVALID INPUT. Please respond with one of the following: "

def test_check_repeating_letter():
    """Test the check_repeating_letter function."""
    assert game.check_repeating_letter(np.array(["X", "X", ""])) == False
    assert game.check_repeating_letter(np.array(["X", "X", "X"])) == True

def test_check_game_over():
    """Test the check_game_over function."""
    game.board = np.array([["X", "X", "X"], ["", "", ""], ["", "", ""]]) 
    assert game.check_game_over() == True
    game.board = np.array([["X", "", "X"], ["", "O", "O"], ["X", "", ""]])
    assert game.check_game_over() == False
    game.board = np.array([["X", "", ""], ["X", "O", "O"], ["X", "", ""]])
    assert game.check_game_over() == True
    game.board = np.array([["X", "O", "X"], ["X", "O", "X"], ["O", "X", "O"]])
    assert game.check_game_over() == True

def test_winning_player():
    """Test the winning player function."""
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
    """Test the 31 lines of code dedicated to the computer's play."""
    if game.game_mode == "2":
        game.board = np.array([["O", "X", "X"], ["", "X", ""], ["", "O", "O"]])
        assert game.computer_play() == 7
    else:
        pass

# def test_play_again(monkeypatch):
#     inputs = (['Y', 'N'])
#     for response in inputs:
#         monkeypatch.setattr('builtins.input', lambda _: response)
#         # go about using input() like you normally would:
#         a = game.play_again()
#         assert a == response