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

        self.moveFunction = {
            'p': self.getPawnMoves, 'R': self.getRookMoves, 'N': self.getKnightMoves,
            'B': self.getBishopMoves, 'Q': self.getQueenMoves, 'K': self.getKingMoves}
        
        self.whiteToMove = True
        self.moveLog = []


    '''
    Tar et trekk som parameter og utfører det. Funker ikke for rokade, en-passant eller forfremmelse
    '''
    def makeMove(self, move):
        if self.board[move.startRow][move.startCol] == "--":
            return None # Ikke gjør noe hvis første rute trykt på er tom
        else:
            self.board[move.startRow][move.startCol] = "--" # Når en brikke flyttes er ruten den dro fra tom
            self.board[move.endRow][move.endCol] = move.pieceMove
            self.moveLog.append(move) # Loggfør trekk for å kunne angre trekk eller vise trekkhistorie
            self.whiteToMove = not self.whiteToMove # Bytte spiller

    
    '''
    Lar bruker angre tidligere trekk
    '''
    def undoMove(self):
        if len(self.moveLog) != 0: # Må ha blitt gjort et trekk før man kan angre
            move = self.moveLog.pop() # Fjerner siste element lagt til i moveLog
            self.board[move.startRow][move.startCol] = move.pieceMove # Sette tilbake til tidligere plass
            self.board[move.endRow][move.endCol] = move.pieceCaptured # Sette mulige tatte brikker tilbake
            self.whiteToMove = not self.whiteToMove # Bytte spiller tilbake
        else:
            print('Må ha blitt gjort et trekk først')


    '''
    Alle trekk som inneholder å sette konge i sjakk
    '''
    def getValidMoves(self):
        return self.getAllPossibleMoves() # Ikke bekymret om sjakk nå


    '''
    Alle trekk uten å inneholde å sette kongen i sjakk
    '''
    def getAllPossibleMoves(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn = self.board[row][col][0] # Se på farge på brikke på en rute
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[row][col][1] # Se på type på brikke på en rute
                    self.moveFunction[piece](row, col, moves) # Kall riktig bevegelsesfunksjon

        return moves


    '''
    Finn alle mulige trekk til bond på rad og kolonne og legg de til listen
    Tar ikke hensyn til en-passant eller forfremmelse
    '''
    def getPawnMoves(self, row, col, moves):
        if self.whiteToMove: # Hvit trekk
            if self.board[row - 1][col] == "--": # En rute bevegelse. -1 siden hvit bonde beveger seg oppover
                moves.append(Move((row, col), (row - 1, col), self.board))
                if row == 6 and self.board[row - 2][col] == "--": # Hvis bonden er på sin original posisjon og kan bevege seg to ruter
                    moves.append(Move((row, col), (row - 2, col), self.board))
            if col - 1 >= 0: # Ta brikke mot venstre. Passe på at bonden ikke går utenfor brettet
                if self.board[row - 1][col - 1][0] == 'b': # Motstanders brikke kan tas
                    moves.append(Move((row, col), (row - 1, col - 1), self.board))
            if col + 1 <= 7: # Ta brikke mot høyre
                if self.board[row - 1][col + 1][0] == 'b': # Motstanders brikke kan tas
                    moves.append(Move((row, col), (row - 1, col + 1), self.board))
        else: # Svart trekk
            if self.board[row + 1][col] == "--": # En rute bevegelse. +1 siden svart bonde beveger seg nedover
                moves.append(Move((row, col), (row + 1, col), self.board))
                if row == 1 and self.board[row + 2][col] == "--": # Hvis bonden er på sin original posisjon og kan bevege seg to ruter
                    moves.append(Move((row, col), (row + 2, col), self.board))
            if col - 1 >= 0: # Ta brikke mot venstre. Passe på at bonden ikke går utenfor brettet
                if self.board[row + 1][col -1][0] == 'w': # Motstanders brikke kan tas
                    moves.append(Move((row, col), (row + 1, col - 1), self.board))
            if col + 1 <= 7: # Ta brikke mot høyre
                if self.board[row + 1][col + 1][0] == 'w': # Motstanders brikke kan tas
                    moves.append(Move((row, col), (row + 1, col + 1), self.board))

    '''
    Finn alle mulige trekk til tårn på rad og kolonne og legg de til listen
    '''
    def getRookMoves(self, row, col, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1)) # Opp, venstre, ned, høyre
        enemyColor = 'b' if self.whiteToMove else 'w'
        for direction in directions:
            for i in range(1, 8): # Det lengste et tårn kan bevege seg er 7 ruter
                endRow = row + direction[0] * i
                endCol = col + direction[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8: # Holde seg innenfor brettet
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--": # Legg til alle mulige plasser som er ledige til moves
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColor: # Legg til plass med motstanders brikke, må stoppe på den ruta
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                        break
                    else: # Vennlig brikke på plass
                        break
                else: # Holde seg på brettet
                    break


    '''
    Finn alle mulige trekk til løper på rad og kolonne og legg de til listen
    Eneste forskjellen fra getRookMoves er directions variabelen
    '''
    def getBishopMoves(self, row, col, moves):
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1)) # (venstre opp), (høyre opp), (venstre ned), (høyre ned)
        enemyColor = 'b' if self.whiteToMove else 'w'
        for direction in directions:
            for i in range(1, 8):
                endRow = row + direction[0] * i
                endCol = col + direction[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8: # Holde seg innenfor brettet
                    endPiece = self.board[endRow][endCol]
                    if endPiece == "--": # Legg til alle mulige plasser som er ledige til moves
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                    elif endPiece[0] == enemyColor: # Legg til plass med motstanders brikke, må stoppe på den ruta
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                        break
                    else: # Vennlig brikke på plass
                        break
                else: # Holde seg på brettet
                    break



    '''
    Finn alle mulige trekk til springer på rad og kolonne og legg de til listen
    '''
    def getKnightMoves(self, row, col, moves):
        movement = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)) # Hopper i en L
        allyColor = 'w' if self.whiteToMove else 'b'
        for squares in movement:
            endRow = row + squares[0]
            endCol = col + squares[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColor: # Tom plass eller motstanders brikke på plass
                    moves.append(Move((row, col), (endRow, endCol), self.board))


    '''
    Finn alle mulige trekk til dronning på rad og kolonne og legg de til listen
    '''
    def getQueenMoves(self, row, col, moves):
        # En dronning er løper og tårn kombinert
        self.getBishopMoves(row, col, moves)
        self.getRookMoves(row, col, moves)


    '''
    Finn alle mulige trekk til konge på rad og kolonne og legg de til listen
    '''
    def getKingMoves(self, row, col, moves):
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)) # Samme som dronning
        allyColor = 'w' if self.whiteToMove else 'b'
        for squares in directions: # Kan kun bevege seg en rute om gangen
            endRow = row + squares[0]
            endCol = col + squares[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColor: # Tom plass eller motstanders brikke på plass
                    moves.append(Move((row, col), (endRow, endCol), self.board))


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
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol


    '''
    Override equals metoden 
    '''
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

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

