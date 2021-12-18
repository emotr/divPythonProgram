# Printer brettet
def printBrett():
    print('-------------------')
    print('| ', brett[0][0], ' | ', brett[0][1], ' | ', brett[0][2], ' |')
    print('-------------------')
    print('| ', brett[1][0], ' | ', brett[1][1], ' | ', brett[1][2], ' |')
    print('-------------------')
    print('| ', brett[2][0], ' | ', brett[2][1], ' | ', brett[2][2], ' |')
    print('-------------------')

# Lar spiller skrive inn tegn
def skrivInnTegn():
    print(hvemsTur, ' sin tur')
    try:
        radNr = int(input('Skriv inn radNr: '))
        kolNr = int(input('Skriv inn kolonneNr: '))

        if sjekkOmPlassErTatt(radNr, kolNr):
            if hvemsTur == 'X':
                brett[radNr][kolNr] = 'X'
            else:
                brett[radNr][kolNr] = 'O'
    except IndexError:
        print('Input må være fra og med 0 til og med 2')

# Sjekker om en plass er tatt så ingenting kan plasseres der
def sjekkOmPlassErTatt(radNr, kolNr):
    if brett[radNr][kolNr] != ' ':
        return False
    
    return True

# Bytter spiller
def bytteSpiller():
    if hvemsTur == 'X':
        return 'O'
    else:
        return 'X'

# Sjekker om brettet er fylt opp
def sjekkOmFull():
    for i in range(3):
        for j in range(3):
            if brett[i][j] == ' ':
                return True
    
    return False

# Sjekker om en spiller har vunnet
def harVunnet():
    for i in range(3):
        if brett[i][0] == hvemsTur and brett[i][1] == hvemsTur and brett[i][2] == hvemsTur:
            return True
        
    for i in range(3):
        if brett[0][i] == hvemsTur and brett[1][i] == hvemsTur and brett[2][i] == hvemsTur:
            return True

    if brett[0][0] == hvemsTur and brett[1][1] == hvemsTur and brett[2][2] == hvemsTur:
        return True

    if brett[0][2] == hvemsTur and brett[1][1] == hvemsTur and brett[2][0] == hvemsTur:
        return True

    return False

hvemsTur = 'X'
brett = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

printBrett()

while sjekkOmFull():
    skrivInnTegn()
    printBrett()

    if harVunnet():
        print(hvemsTur, ' har vunnet!')
        break
    
    hvemsTur = bytteSpiller()