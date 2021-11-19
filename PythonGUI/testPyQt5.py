from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300) # 200 x 200 er hvor på skjermen vinduet kommer opp fra øvre venstre hjørne
                                        # 300 x 300 er størrelsen på selve vinduet
    win.setWindowTitle("Yeet")

    label = QtWidgets.QLabel(win)
    label.setText("My first label!")
    label.move(50, 50) # 50 x 50 fra øvre venstre hjørne

    win.show()
    sys.exit(app.exec_())

window()