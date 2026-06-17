import io

from game import Game
from textwrap import dedent

def test_print_board(capsys):
    game = Game("X", "O")
    game.play(2, 1)
    game.print_board()
    out, err = capsys.readouterr()
    assert out.strip() == dedent("""
                         . . .
                         . . .
                         . X .
                         """).strip()

def test_full_play(capsys, monkeypatch):
    game = Game("X", "O")
    monkeypatch.setattr("sys.stdin", io.StringIO('\n'.join([
        '(0, 0)',
        '(1, 0)',
        '(0, 1)',
        '(1, 1)',
        '(0, 2)'
    ])))
    # run full game loop
    game.main()

    out, err = capsys.readouterr()
    assert out.strip() == dedent("""
        . . .
        . . .
        . . .

        X's turn: X . .
        . . .
        . . .

        O's turn: X . .
        O . .
        . . .

        X's turn: X X .
        O . .
        . . .

        O's turn: X X .
        O O .
        . . .

        X's turn: X X X
        O O .
        . . .

        X wins!
        """).strip()
    assert game.winner == "X"

