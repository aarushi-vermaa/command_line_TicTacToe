"""Test Tic Tac Toe classes and functions."""
import pytest
import tic_tac_toe_game as tttg

game = tttg.tic_tac_toe()

def test_enter_postition(monkeypatch):
    """Test Tic Tac Toe."""
    # This simulates the user entering "1" in the terminal:
    monkeypatch.setattr('builtins.input', lambda _: "1")
    responses = iter(['"Position Occupied. Please Try Again.',\
        'Invalid input. Please enter a number between 1 and 9',\
            'Invalid input. Please enter a number between 1 and 9'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    # go about using input() like you normally would:
    monkeypatch.setattr('builtins.input', lambda _: "N")


    # monkeypatch.setattr('builtins.input', lambda _: "1")
