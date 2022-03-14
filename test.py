import chess
import random

board = chess.Board()

running = True
while running == True:
    print('')
    print('------------------')
    print(board)
    print('------------------')
    print('')
    legal_moves = list(board.legal_moves)
    index = int(random.random() * len(legal_moves))
    board.push(legal_moves[index])

    if board.is_checkmate() == True:
        running = False
    if board.is_stalemate() == True:
        running = False
    if board.is_insufficient_material() == True:
        running = False