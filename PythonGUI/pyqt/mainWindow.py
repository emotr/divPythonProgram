from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle("Testing 1 2 3")
        self.initUI()
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self) # lage en label og bestemme hvor det skal settes
        self.label.setText('My first label!')
        self.label.move(50,50) # x og y-koordinater fra øvre venstre hjørne

        self.b1 = QtWidgets.QPushButton(self) # lager en knapp og setter den i win
        self.b1.setText('Click me!') # setter tekst på knappen
        self.b1.clicked.connect(self.clickedButton) # kobler knappen til funksjonen clickedButton

    def clickedButton(self):
        self.label.setText('You pressed the button')
        self.update()
    
    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show() # for å vise vinduet
    sys.exit(app.exec_())

window()