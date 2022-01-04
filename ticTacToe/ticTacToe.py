from typing import Counter
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QAction, QMessageBox
from PyQt5 import uic
import sys, random

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("ticTacToe.ui", self)

        # Track whose turn it is
        self.counter = 0
        self.whoseTurn = 'X'

        # Track which turn it is
        self.turn = 0

        # Track stats
        self.numberOfXWins = self.numberOfOWins = self.numberOfDraws0 = 0

        # Define widgets
        # Button widgets
        self.button1 = self.findChild(QPushButton, "button_00")
        self.button2 = self.findChild(QPushButton, "button_01")
        self.button3 = self.findChild(QPushButton, "button_02")
        self.button4 = self.findChild(QPushButton, "button_10")
        self.button5 = self.findChild(QPushButton, "button_11")
        self.button6 = self.findChild(QPushButton, "button_12")
        self.button7 = self.findChild(QPushButton, "button_20")
        self.button8 = self.findChild(QPushButton, "button_21")
        self.button9 = self.findChild(QPushButton, "button_22")

        # Reset statistics action and quit action
        self.buttonReset_Statistics.triggered.connect(self.resetStats)
        self.buttonQuit.triggered.connect(self.quit)

        # Label widgets
        self.labelTurn = self.findChild(QLabel, "labelWhoseTurn")
        self.labelTies = self.findChild(QLabel, "label_Ties")
        self.labeloWins = self.findChild(QLabel, "label_oWins")
        self.labelxWins = self.findChild(QLabel, "label_xWins")

        # Click the button
        self.button1.clicked.connect(lambda: self.clicker(self.button1))
        self.button2.clicked.connect(lambda: self.clicker(self.button2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))

        self.show()

    # Click on button to set symbol
    def clicker(self, b):
        if self.whoseTurn == 'X':
            self.labelTurn.setText("Player: O")
        else:
            self.labelTurn.setText("Player: X")
        
        b.setText(self.whoseTurn)
        b.setEnabled(False)

        # Check if a player has won
        self.checkIfWon()

        # Check to see if it's a draw
        self.checkIfFull()

        # Increment counter
        self.counter += 1
        self.swapPlayer()

    def swapPlayer(self):
        if self.counter % 2 == 0:
            self.whoseTurn = 'X'
        else:
            self.whoseTurn = 'O'

    # Reset board if wants to play again
    def resetBoard(self):
        buttonList = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9
        ]

        # Reset buttons
        for button in buttonList:
            button.setText("")
            button.setEnabled(True)
            # Reset the color of the buttons
            button.setStyleSheet('QPushButton  {color: #797979;}')

        # Reset counter and tracker
        self.counter = 0
        self.turn = 0

    # Check if a player has won on their turn
    def checkIfWon(self):
        # Across
        if self.button1.text() == self.button2.text() == self.button3.text() == self.whoseTurn:
            self.hasWon(self.button1, self.button2, self.button3)

        if self.button4.text() == self.button5.text() == self.button6.text() == self.whoseTurn:
            self.hasWon(self.button4, self.button5, self.button6)

        if self.button7.text() == self.button8.text() == self.button9.text() == self.whoseTurn:
            self.hasWon(self.button7, self.button8, self.button9)

        # Down
        if self.button1.text() == self.button4.text() == self.button7.text() == self.whoseTurn:
            self.hasWon(self.button1, self.button4, self.button7)

        if self.button2.text() == self.button5.text() == self.button8.text() == self.whoseTurn:
            self.hasWon(self.button2, self.button5, self.button8)

        if self.button3.text() == self.button6.text() == self.button9.text() == self.whoseTurn:
            self.hasWon(self.button3, self.button6, self.button9)

        # Diagonals
        if self.button1.text() == self.button5.text() == self.button9.text() == self.whoseTurn:
            self.hasWon(self.button1, self.button5, self.button9)

        if self.button3.text() == self.button5.text() == self.button7.text() == self.whoseTurn:
            self.hasWon(self.button3, self.button5, self.button7)

       
    # When a player has won
    def hasWon(self, a, b, c):
        # Set the winning squares to be red
        a.setStyleSheet('QPushButton  {color: red;}')
        b.setStyleSheet('QPushButton  {color: red;}')
        c.setStyleSheet('QPushButton  {color: red;}')
        self.labelTurn.setText(f"{a.text()} Has Won!")

        if(a.text() == 'X'):
            self.numberOfXWins += 1
            self.labelxWins.setText(f"X: {self.numberOfXWins}")
        else:
            self.numberOfOWins += 1
            self.labeloWins.setText(f"O: {self.numberOfOWins}")

        # Disable the board
        self.disable()

        self.winPopup()

    # Check to see if the board is full without a winner
    def checkIfFull(self):
        self.turn += 1
        if self.turn == 9:
            self.labelTurn.setText("It is a tie")
            self.disable()
            self.drawPopup()
            self.numberOfDraws += 1
            self.labelTies.setText(f"Draws: {self.numberOfDraws}")

    # Popup for draws
    def drawPopup(self):
        msg = QMessageBox()
        msg.setText("The game is a tie")
        msg.setWindowTitle("The game is a tie")
        msg.setInformativeText('Play again?')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.Yes)
        msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()

    # Disable all the buttons in the grid when a player wins
    def disable(self):
        buttonList = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9
        ]

        for button in buttonList:
            button.setEnabled(False)

    # Popup message that pops up when a player wins
    def winPopup(self):
        msg = QMessageBox()
        msg.setText(f"{self.whoseTurn} has won!")
        msg.setWindowTitle("We have a winner!")
        msg.setInformativeText('Play again?')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.Yes)

        msg.buttonClicked.connect(self.popup_button)

        x = msg.exec_()

    # Let user respond to popup message
    def popup_button(self, response):
        if response.text() == "&Yes":
            if self.whoseTurn == 'O':
                self.swapPlayer()
            else:
                pass
            self.resetBoard()
            self.labelTurn.setText(f"Player: X")
        else:
            sys.exit()

    # Let user reset statistics
    def resetStats(self):
        self.numberOfXWins = 0
        self.labelxWins.setText(f"X: {self.numberOfXWins}")
        self.numberOfOWins = 0
        self.labeloWins.setText(f"O: {self.numberOfOWins}")
        self.numberOfDraws = 0
        self.labelTies.setText(f"Draws: {self.numberOfDraws}")

    # Let user quit the game from 
    def quit(self):
        sys.exit()
        

# Initialize the application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()