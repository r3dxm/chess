import engine
import pygame as pg

pg.init()

WIDTH = 512
HEIGHT = 512
DIMENSION = 8
SQ_SIZE = WIDTH / DIMENSION
IMAGES = {}

def load_images():
    pieces = ['bK', 'bQ', 'bB', 'bN', 'bR', 'bp', 'wK', 'wQ', 'wB', 'wN', 'wR', 'wp']

    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def main():
    state = engine.gameState()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    load_images()
    running = True
    previous = engine.fen_to_array(state.fen)

    while running == True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        piece_array = engine.fen_to_array(state.fen)
        draw_game_state(screen, piece_array)

def draw_game_state(screen, piece_array):
    draw_board(screen)
    draw_pieces(screen, piece_array)

def draw_board(screen):
    WHITE = (255, 255, 255)
    GREY = (127, 127, 127)

    for x in range(DIMENSION):
        for y in range(DIMENSION):
            if (x + y) % 2 == 0:
                color = WHITE
            else:
                color = GREY

            pg.draw.rect(screen, color, pg.Rect(x * SQ_SIZE, y * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            pg.display.flip()

def draw_pieces(screen, piece_array):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            piece = piece_array[j][i]
            if piece != '':
                screen.blit(IMAGES[piece], pg.Rect(i * SQ_SIZE, j * SQ_SIZE, SQ_SIZE, SQ_SIZE))


main()