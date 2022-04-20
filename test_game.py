"""Test Tic Tac Toe classes and functions."""
import pytest
from tic_tac_toe_game.py import tic_tac_toe


def test_tic_tac_toe(monkeypatch):
    """Test Tic Tac Toe."""
    game = tic_tac_toe()
    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setattr('builtins.input', lambda _: "1")

    # go about using input() like you normally would:
    i = input("Please enter the position:")
    assert i == "1"