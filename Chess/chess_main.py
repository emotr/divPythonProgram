"""
Driver fil. Håndtere brukerinput og vise nåværende informasjon om spillet
"""

import pygame as p
import chess_engine

WIDTH = HEIGHT = 512 # Vindustørrelse. Burde være delelig med 2
DIMENSION = 8 # Dimensjonene til et sjakkbrett er 8x8
SQ_SIZE = HEIGHT // DIMENSION # Størrelse på rute
MAX_FPS = 15 # For løkkehastighet og animasjon senere i prosjektet
IMAGES = {}

''' 
Initialiser en global dictionary av bilder. Kalles en gang i main
'''
def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("pieces/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    
    # Kan nå få tilgang til et bilde ved å si 'IMAGES['wp']'


'''
Main driver kode. Håndtere brukerinput og oppdatere grafikk
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    start_screen_settings(screen)

    clock = p.time.Clock()
    gs = chess_engine.GameState()
    load_images() # Bare gjøre dette en gang, før while løkka
    
    running = True
    sqSelected = () # Ingen rute er valgt til å begynne med, holde følge med hvilken rute som er valgt (tuple: rad, kolonne)
    playerClick = [] # Holde følge med spiller trykk (to tupler: [(6, 4), (4, 4)])
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                
            # Peker håndtering
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x, y) lokasjon til peker
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col): # Bruker trykte på samme rute to ganger
                    sqSelected = () # deselect
                    playerClick = [] # Tøm spiller trykk
                else:
                    sqSelected = (row, col)
                    playerClick.append(sqSelected) # Legg til både første og andre trykk
                if len(playerClick) == 2: # Etter andre trykk
                    move = chess_engine.Move(playerClick[0], playerClick[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = () # Reset spillertrykk
                    playerClick = [] 

            # Tastatur håndtering
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: # Angre når bruker trykker på 'z'
                    gs.undoMove()

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Sett vindutittel, ikon og bakgrunnsfarge i vinduet
'''
def start_screen_settings(screen):
    p.display.set_caption("Chess")
    icon = p.image.load('pieces/wK.png')
    p.display.set_icon(icon)
    screen.fill(p.Color("white"))


'''
Ansvarlig for all grafikk innenfor nåværende game state
'''
def drawGameState(screen, gs):
    drawBoard(screen) # Tegne ruter på brettet
    # Kan legge til ting som brikke highlighting, trekk foreslag etc (senere)
    drawPieces(screen, gs.board) # Tegn brikker oppå brettet


'''
Tegne ruter på brettet
'''
def drawBoard(screen):
    colors = [p.Color(204, 183, 174), p.Color(112, 102, 109)] # Lys rute, mørk rute
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row+col) % 2)]
            p.draw.rect(screen, color, p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Tegne brikker på brettet ved å bruke GameState.board
'''
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            if piece != "--": # Ikke tom rute
                screen.blit(IMAGES[piece], p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()