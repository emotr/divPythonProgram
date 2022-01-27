"""
Denne klassen skal lagre all informasjon om nåværende state av et sjakkparti.
Også ansvarlig for å bestemme gyldige trekk i nåværende state.
Også holde på en trekklogg.
"""
import boards

class GameState():
    def __init__(self):
        self.board = boards.patt # Last inn et brett fra Boards

        self.moveFunction = {
            'p': self.getPawnMoves, 'R': self.getRookMoves, 'N': self.getKnightMoves,
            'B': self.getBishopMoves, 'Q': self.getQueenMoves, 'K': self.getKingMoves}
        
        self.whiteToMove = True
        self.moveLog = []
        self.whiteKingLocation = (7,4)
        self.blackKingLocation = (0, 4)
        self.inCheck = False
        self.pins = []
        self.checks = []



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
            if move.pieceMove == 'wK': # Oppdatere kongens posisjon hvis den ble flyttet
                self.whiteKingLocation = (move.endRow, move.endCol)
            if move.pieceMove == 'bK': # Oppdatere kongens posisjon hvis den ble flyttet
                self.blackKingLocation = (move.endRow, move.endCol)


    
    '''
    Lar bruker angre tidligere trekk
    '''
    def undoMove(self):
        if len(self.moveLog) != 0: # Må ha blitt gjort et trekk før man kan angre
            move = self.moveLog.pop() # Fjerner siste element lagt til i moveLog
            self.board[move.startRow][move.startCol] = move.pieceMove # Sette tilbake til tidligere plass
            self.board[move.endRow][move.endCol] = move.pieceCaptured # Sette mulige tatte brikker tilbake
            self.whiteToMove = not self.whiteToMove # Bytte spiller tilbake
            if move.pieceMove == 'wK': # Oppdatere kongens posisjon hvis den ble flyttet
                self.whiteKingLocation = (move.startRow, move.startCol)
            if move.pieceMove == 'bK': # Oppdatere kongens posisjon hvis den ble flyttet
                self.blackKingLocation = (move.startRow, move.startCol)
        else:
            print('Må ha blitt gjort et trekk først')


    '''
    Alle trekk som inneholder å sette konge i sjakk
    '''
    def getValidMoves(self):
        moves = []
        self.inCheck, self.pins, self.checks = self.checkForPinsAndChecks()
        if self.whiteToMove:
            kingRow = self.whiteKingLocation[0]
            kingCol = self.whiteKingLocation[1]
        else:
            kingRow = self.blackKingLocation[0]
            kingCol = self.blackKingLocation[1]
        if self.inCheck:
            if len(self.checks) == 1: # Kun en sjakk, kan blokkere, ta eller flytte kongen
                moves = self.getAllPossibleMoves()
                check = self.checks[0] # Info om sjakk
                checkRow = check[0]
                checkCol = check[1]
                pieceChecking = self.board[checkRow][checkCol] # Motstanders brikke som setter kongen i sjakk
                validSquares = [] # Ruter brikker kan bevege seg til
                if pieceChecking[1] == 'N': # Kan ikke blokkere sjakk fra hest
                    validSquares[(checkRow, checkCol)]
                else: # Kan blokkere andre brikker enn hest
                    for i in range(1, 8):
                        validSquare = (kingRow + check[2] * i, kingCol + check[3] * i)
                        validSquares.append(validSquare)
                        if validSquare[0] == checkRow and validSquare[1] == checkCol:
                            break
                
                # Fjern trekk som ikke blokkerer sjakk eller flytter konge
                for i in range(len(moves) - 1, -1, -1): # Gå gjennom baklengs
                    if moves[i].pieceMove[1] != 'K': # Trekk flytter ikke konge, så må blokkere eller ta
                        if not (moves[i].endRow, moves[i].endCol) in validSquares:
                            moves.remove(moves[i])
            else: # Dobbel sjakk, konge må flytte seg
                self.getKingMoves(kingRow, kingCol, moves)
        else: # Ikke i sjakk så alle trekk er gyldige
            moves = self.getAllPossibleMoves()
        
        return moves



    def checkForPinsAndChecks(self):
        pins = []
        checks = []
        inCheck = False
        if self.whiteToMove:
            enemyColor = 'b'
            allyColor = 'w'
            startRow = self.whiteKingLocation[0]
            startCol = self.whiteKingLocation[1]
        else:
            enemyColor = 'w'
            allyColor = 'b'
            startRow = self.blackKingLocation[0]
            startCol = self.blackKingLocation[1]
        # Sjekk fra kongen for pins og sjakk
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        for j in range(len(directions)):
            d = directions[j]
            possiblePin = ()
            for i in range(1, 8):
                endRow = startRow + d[0] * i
                endCol = startCol + d[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endPiece = self.board[endRow][endCol]
                    if endPiece[0] == allyColor and endPiece[1] != 'K':
                        if possiblePin == (): # Første alliert brikke som kan spiddes
                            possiblePin = (endRow, endCol, d[0], d[1])
                        else: # To eller mer allierte brikker så ingen mulige spiddinger i denne retning
                                break
                    elif endPiece[0] == enemyColor:
                        type = endPiece[1] # Se på hva slags brikke det er
                        # Fem muligheter i if testen under
                        # 1. Ortogonalt fra kongen og brikken er et tårn
                        # 2. Diagonalt fra kongen og brikken er en løper
                        # 3. En rute fra kongen og brikken er en bonde
                        # 4. Enhver retning og brikken er en dronning
                        # 5. Enhver retning og brikken er en konge (Nødvendig for å forhindre 
                        # en konge til å bevege seg til en rute kontrollert av den andre kongen)
                        if (0 <= j <= 3 and type == 'R') or \
                                (4 <= j <= 7 and type == 'B') or \
                                (i == 1 and type == 'p' and ((enemyColor == 'w' and 6 <= j <= 7) or \
                                (enemyColor == 'b' and  4 <= j <= 5))) or \
                                (type == 'Q') or (i == 1 and type == 'K'):
                            if possiblePin == (): # Ingen brikke blokkerer
                                inCheck = True
                                checks.append((endRow, endCol, d[0], d[1]))
                                break
                            else: # Brikke blokkerer så spidding
                                pins.append(possiblePin)
                                break
                        else: # Motstander brikke setter ikke konge i sjakk
                            break
                else: # Av brettet
                    break
        # Sjekk for springer sjakk
        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2))
        for move in knightMoves:
            endRow = startRow + move[0]
            endCol = startCol + move[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] == enemyColor and endPiece[1] == 'N':
                    inCheck = True
                    checks.append((endRow, endCol, move[0], move[1]))
        return inCheck, pins, checks


                
    '''
    Angi om current spiller er i sjakk
    '''
    def inCheck(self):
        if self.whiteToMove:
            return self.squareUnderAttack(self.whiteKingLocation[0], self.whiteKingLocation[1])
        else:
            return self.squareUnderAttack(self.blackKingLocation[0], self.blackKingLocation[1])


    '''
    Angi om motstander kan angripe rute (row, col)
    '''
    def squareUnderAttack(self, row, col):
        self.whiteToMove = not self.whiteToMove # Bytte til motstander sin tur
        oppMoves = self.getAllPossibleMoves()
        self.whiteToMove = not self.whiteToMove # Bytte tilbake
        for move in oppMoves:
            if move.endRow == row and move.endCol == col: # Rute under angrep
                return True
        return False

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
        piecePinned = False
        pinDirection = ()
        for i in range(len(self.pins) - 1, -1, -1):
            if self.pins[i][0] == row and self.pins[i][1] == col:
                piecePinned = True
                pinDirection = (self.pins[i][2], self.pins[i][3])
                self.pins.remove(self.pins[i])
            break

        # Hvit trekk
        if self.whiteToMove: 
            if self.board[row - 1][col] == "--": # En rute bevegelse
                if not piecePinned or pinDirection == (-1, 0):
                    moves.append(Move((row, col), (row - 1, col), self.board))
                    if row == 6 and self.board[row - 2][col] == "--": # To ruter bevegelse
                        moves.append(Move((row, col), (row - 2, col), self.board))
            if col - 1 >= 0: # Ta mot venstre
                if self.board[row - 1][col - 1][0] == 'b':
                    if not piecePinned or pinDirection == (-1, -1):
                        moves.append(Move((row, col), (row - 1, col - 1), self.board))
            if col + 1 <= 7: # Ta mot høyre
                if self.board[row - 1][col + 1][0] == 'b':
                    if not piecePinned or pinDirection == (-1, 1):
                        moves.append(Move((row, col), (row - 1, col + 1), self.board))
        # Svart trekk
        else:
            if self.board[row + 1][col] == "--": # En rute bevegelse. +1 siden svart bonde beveger seg nedover
                if not piecePinned or pinDirection == (1, 0):
                    moves.append(Move((row, col), (row + 1, col), self.board))
                    if row == 1 and self.board[row + 2][col] == "--": # Hvis bonden er på sin original posisjon og kan bevege seg to ruter
                        moves.append(Move((row, col), (row + 2, col), self.board))
            if col - 1 >= 0: # Ta brikke mot venstre. Passe på at bonden ikke går utenfor brettet
                if self.board[row + 1][col - 1][0] == 'w': # Motstanders brikke kan tas
                    if not piecePinned or pinDirection == (1, -1):
                        moves.append(Move((row, col), (row + 1, col - 1), self.board))
            if col + 1 <= 7: # Ta brikke mot høyre
                if self.board[row + 1][col + 1][0] == 'w': # Motstanders brikke kan tas
                    if not piecePinned or pinDirection == (1, 1):
                        moves.append(Move((row, col), (row + 1, col + 1), self.board))

    '''
    Finn alle mulige trekk til tårn på rad og kolonne og legg de til listen
    '''
    def getRookMoves(self, row, col, moves):
        piecePinned = False
        pinDirection = ()
        for i in range(len(self.pins)-1, -1, -1):
            if self.pins[i][0] == row and self.pins[i][1] == col:
                piecePinned = True
                pinDirection = (self.pins[i][2], self.pins[i][3])
                if self.board[row][col][1] != 'Q':
                    self.pins.remove(self.pins[i])
                break
        
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1)) # Opp, venstre, ned, høyre
        enemyColor = 'b' if self.whiteToMove else 'w'
        for direction in directions:
            for i in range(1, 8): # Det lengste et tårn kan bevege seg er 7 ruter
                endRow = row + direction[0] * i
                endCol = col + direction[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8: # Holde seg innenfor brettet
                    if not piecePinned or pinDirection == direction or pinDirection == (-direction[0], -direction[1]):
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
        piecePinned = False
        pinDirection = ()
        for i in range(len(self.pins)-1, -1, -1):
            if self.pins[i][0] == row and self.pins[i][1] == col:
                piecePinned = True
                pinDirection = (self.pins[i][2], self.pins[i][3])
                self.pins.remove(self.pins[i])
                break

        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1)) # (venstre opp), (høyre opp), (venstre ned), (høyre ned)
        enemyColor = 'b' if self.whiteToMove else 'w'
        for direction in directions:
            for i in range(1, 8):
                endRow = row + direction[0] * i
                endCol = col + direction[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8: # Holde seg innenfor brettet
                    if not piecePinned or pinDirection == direction or pinDirection == (-direction[0], -direction[1]):
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
        piecePinned = False
        for i in range(len(self.pins)-1, -1, -1):
            if self.pins[i][0] == row and self.pins[i][1] == col:
                piecePinned = True
                pinDirection = (self.pins[i][2], self.pins[i][3])
                self.pins.remove(self.pins[i])
                break
        
        movement = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2)) # Hopper i en L
        allyColor = 'w' if self.whiteToMove else 'b'
        for squares in movement:
            endRow = row + squares[0]
            endCol = col + squares[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                if not piecePinned:
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
        rowMoves = (-1, -1, -1, 0, 0, 1, 1, 1)
        colMoves = (-1, 0, 1, -1, 1, -1, 0, 1)
        allyColor = 'w' if self.whiteToMove else 'b'
        for i in range(8):
            endRow = row + rowMoves[i]
            endCol = col + colMoves[i]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endPiece = self.board[endRow][endCol]
                if endPiece[0] != allyColor: # Tom eller motstanders brikke på rute
                    # Plasser konge på enderute og sjekk for sjakk
                    if allyColor == 'w':
                        self.whiteKingLocation = (endRow, endCol)
                    else:
                        self.blackKingLocation = (endRow, endCol)
                    inCheck, pins, checks = self.checkForPinsAndChecks()
                    if not inCheck:
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                    # Plasser konge tilbake til original plass
                    if allyColor == 'w':
                        self.whiteKingLocation = (row, col)
                    else:
                        self.blackKingLocation = (row, col)


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

