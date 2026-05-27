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
