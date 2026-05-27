import pytest
from game import Game, InvalidMoveError

def test_empty_board():
    game = Game("X", "O")
    for i in range(3):
        for j in range(3):
            assert game.get(i, j) == ""

def test_can_play():
    game = Game("X", "O")
    game.play(1, 1)
    assert game.get(1, 1) == "X"

def test_cant_play_twice():
    game = Game("X", "O")
    game.play(1, 1)
    with pytest.raises(InvalidMoveError):
        game.play(1, 1)

def test_cant_play_outside():
    game = Game("X", "O")
    with pytest.raises(InvalidMoveError):
        game.play(5, 5)

def test_win():
    game = Game("X", "O")
    game.play(0, 0)  # X plays
    game.play(1, 0)  # O plays
    game.play(0, 1)  # X plays
    game.play(1, 1)  # O plays
    game.play(0, 2)  # X plays
    assert game.winner == "X"

def test_tie():
    game = Game("X", "O")
    game.play(0, 0)  # X plays
    game.play(0, 1)  # O plays
    game.play(0, 2)  # X plays
    game.play(1, 2)  # O plays
    game.play(1, 0)  # X plays
    game.play(2, 0)  # O plays
    game.play(1, 1)  # X plays
    game.play(2, 2)  # O plays
    game.play(2, 1)  # X plays
    assert game.winner is None
    assert game.is_tie()

