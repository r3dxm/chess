import chess
import random

class gameState():
    def __init__(self):
        self.board = chess.Board()
        self.white_to_move = chess.WHITE
        self.legal_moves = self.board.legal_moves
        self.castling_rights = bool(self.board.castling_rights)
        self.fen = self.board.board_fen()

    def random_move(board):
        legal_moves = list(board.legal_moves)
        index = random.random(len(legal_moves))

        return legal_moves[index]

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