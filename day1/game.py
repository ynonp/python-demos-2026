class InvalidMoveError(Exception):
    pass


class Game:
    def __init__(self, player1, player2):
        self._players = [player1, player2]
        self._board = [["" for _ in range(3)] for _ in range(3)]
        self._current_player_index = 0
        self.winner = None
        self._moves_count = 0

    def get(self, i, j):
        return self._board[i][j]

    def play(self, i, j):
        if not (0 <= i < 3 and 0 <= j < 3):
            raise InvalidMoveError("Position out of bounds")
        if self._board[i][j] != "":
            raise InvalidMoveError("Position already occupied")
        if self.winner is not None:
            raise InvalidMoveError("Game already over")

        current_player = self._players[self._current_player_index]
        self._board[i][j] = current_player
        self._moves_count += 1

        if self._check_winner(current_player):
            self.winner = current_player
        else:
            self._current_player_index = 1 - self._current_player_index

    def _check_winner(self, player):
        # Check rows
        for row in range(3):
            if all(self._board[row][col] == player for col in range(3)):
                return True
        # Check columns
        for col in range(3):
            if all(self._board[row][col] == player for row in range(3)):
                return True
        # Check diagonals
        if all(self._board[i][i] == player for i in range(3)):
            return True
        if all(self._board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_tie(self):
        return self.winner is None and self._moves_count == 9

    def print_board(self):
        for i in range(3):
            line = []
            for j in range(3):
                val = self._board[i][j]
                line.append(val if val else ".")
            print(" ".join(line))
        print()
