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
                y += 1
            if c == 'Q':
                array[x][y] = 'wQ'
                y += 1
            if c == 'B':
                array[x][y] = 'wB'
                y += 1
            if c == 'N':
                array[x][y] = 'wN'
                y += 1
            if c == 'R':
                array[x][y] = 'wR'
                y += 1
            if c == 'P':
                array[x][y] = 'wp'
                y += 1
            if c == 'k':
                array[x][y] = 'bK'
                y += 1
            if c == 'q':
                array[x][y] = 'bQ'
                y += 1
            if c == 'b':
                array[x][y] = 'bB'
                y += 1
            if c == 'n':
                array[x][y] = 'bN'
                y += 1
            if c == 'r':
                array[x][y] = 'bR'
                y += 1
            if c == 'p':
                array[x][y] = 'bp'
                y += 1
            if c == '/':
                y = 0
                x += 1
            if c == '2':
                y += 2
            if c == '3':
                y += 3
            if c == '4':
                y += 4
            if c == '5':
                y += 5
            if c == '6':
                y += 6
            if c == '7':
                y += 7
            if c == '8':
                y += 8

        return array