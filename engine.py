import chess
import random

class gameState():
    def __init__(self):
        self.board = chess.Board()
        self.white_to_move = chess.WHITE
        self.legal_moves = self.board.legal_moves
        self.castling_rights = bool(self.board.castling_rights)
        self.fen = self.board.board_fen()

    def make_move(self, move):
        to_move = chess.Move.from_uci(move.notation())
        if to_move in self.legal_moves:
            self.board.push(to_move)
            self.fen = self.board.board_fen()
            self.legal_moves = self.board.legal_moves

class move():
    ranks_rows = {
        "1": 7,
        "2": 6,
        "3": 5,
        "4": 4,
        "5": 3,
        "6": 2,
        "7": 1,
        "8": 0
    }
    rows_ranks = {v: k for k, v in ranks_rows.items()}

    files_cols = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
    }
    cols_files = {v: k for k, v in files_cols.items()}

    def __init__(self, start_sq, end_sq, board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_capt = board[self.end_row][self.end_col]

    def notation(self):
        return self.get_rankfile(self.start_row, self.start_col) + self.get_rankfile(self.end_row, self.end_col)

    def get_rankfile(self, row, col):
        return self.cols_files[col] + self.rows_ranks[row]

def fen_to_array(fen):
        array = [['' for i in range(8)] for j in range(8)]

        fen_list = list(fen)

        x = 0
        y = 0
        for c in fen_list:
            if c == 'K':
                array[x][y] = 'wK'
                x += 1
            if c == 'Q':
                array[x][y] = 'wQ'
                x += 1
            if c == 'B':
                array[x][y] = 'wB'
                x += 1
            if c == 'N':
                array[x][y] = 'wN'
                x += 1
            if c == 'R':
                array[x][y] = 'wR'
                x += 1
            if c == 'P':
                array[x][y] = 'wp'
                x += 1
            if c == 'k':
                array[x][y] = 'bK'
                x += 1
            if c == 'q':
                array[x][y] = 'bQ'
                x += 1
            if c == 'b':
                array[x][y] = 'bB'
                x += 1
            if c == 'n':
                array[x][y] = 'bN'
                x += 1
            if c == 'r':
                array[x][y] = 'bR'
                x += 1
            if c == 'p':
                array[x][y] = 'bp'
                x += 1
            if c == '/':
                x = 0
                y += 1
            if c == '1':
                x += 1
            if c == '2':
                x += 2
            if c == '3':
                x += 3
            if c == '4':
                x += 4
            if c == '5':
                x += 5
            if c == '6':
                x += 6
            if c == '7':
                x += 7
            if c == '8':
                x += 8

        return array