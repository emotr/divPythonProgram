from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    #win.setGeometry(xpos, ypos, width, height) # x og ypos er fra øvre venstre hjørne
    win.setGeometry(100, 100, 300, 300)
    win.setWindowTitle("Testing 1 2 3")

    label = QtWidgets.QLabel(win) # lage en label og bestemme hvor det skal settes
    label.setText('My first label!')
    label.move(50,50) # x og y-koordinater fra øvre venstre hjørne

    win.show() # for å vise vinduet
    sys.exit(app.exec_())

window()