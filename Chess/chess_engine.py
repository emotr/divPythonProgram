"""
Denne klassen skal lagre all informasjon om nåværende state av et sjakkparti.
Også ansvarlig for å bestemme gyldige trekk i nåværende state.
Også holde på en trekklogg.
"""
class GameState():
    def __init__(self):
        # Board er en 8x8 2d liste, der hvert element er bygd opp av to karakterer
        # Første karakter er farge på brikke. Andre karakter er type brikke
        # "--" representerer en tom rute uten en brikke
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        if self.board[move.startRow][move.startCol] == "--":
            return None # Ikke gjør noe hvis første rute trykt på er tom
        else:
            self.board[move.startRow][move.startCol] = "--" # Når en brikke flyttes er ruten den dro fra tom
            self.board[move.endRow][move.endCol] = move.pieceMove
            self.moveLog.append(move) # Loggfør trekk for å kunne angre trekk eller vise trekkhistorie
            self.whiteToMove = not self.whiteToMove # Bytte spiller


class Move():
    # Map nøkler til verdier for å kunne bruke sjakknotasjon
    # nøkkel : verdi
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMove = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]


    '''
    Skriver ut hvilket trekk som gjøres
    '''
    def getChessNotation(self):
        # TODO: Rokade, sette konge i sjakk, sjakkmatt, forfremmelse
        notation = ""
        if self.pieceCaptured == "--":
            notation = self.pieceMove + self.getRankFile(self.endRow, self.endCol)
            notation = notation[1:] # Fjerner w eller b fra brikker men ikke bønder
            if self.pieceMove == "wp" or self.pieceMove == "bp": # Når en bonde flyttes inkluderes ikke p
                notation = notation[1:]
        elif self.pieceCaptured != "--": # Inkluder x når en brikke tas 
            notation = self.pieceMove + "x" + self.getRankFile(self.endRow, self.endCol)
            notation = notation[1:] # Fjerner w eller b fra brikker men ikke bønder
            if self.pieceMove == "wp" or self.pieceMove == "bp": # Når en bonde tar en brikke
                notation = self.getFile(self.startCol) + "x" + self.getRankFile(self.endRow, self.endCol)
            
        return notation


    '''
    Returnerer kolonneNr til filNr og radNr til rankNr for å bruke ordentlig sjakknotasjon
    '''
    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]


    '''
    Returner kolonneNr til filNr når bønder tar brikker i utskrift
    '''
    def getFile(self, c):
        return self.colsToFiles[c]

