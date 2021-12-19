# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logicgate.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# En logisk port kalkulator
# Regner ut AND, OR, XOR, NAND, NOR, XNOR for to input verdier


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/ANDgate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboX = QtWidgets.QComboBox(self.centralwidget)
        self.comboX.setGeometry(QtCore.QRect(10, 50, 191, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboX.setFont(font)
        self.comboX.setObjectName("comboX")
        self.comboX.addItem("")
        self.comboX.addItem("")
        self.comboY = QtWidgets.QComboBox(self.centralwidget)
        self.comboY.setGeometry(QtCore.QRect(310, 50, 191, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboY.setFont(font)
        self.comboY.setObjectName("comboY")
        self.comboY.addItem("")
        self.comboY.addItem("")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(10, 250, 191, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.comboPickGate = QtWidgets.QComboBox(self.centralwidget)
        self.comboPickGate.setGeometry(QtCore.QRect(310, 250, 191, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboPickGate.setFont(font)
        self.comboPickGate.setObjectName("comboPickGate")
        self.comboPickGate.addItem("")
        self.comboPickGate.addItem("")
        self.comboPickGate.addItem("")
        self.comboPickGate.addItem("")
        self.comboPickGate.addItem("")
        self.comboPickGate.addItem("")
        self.comboPickGate.addItem("")
        self.comboPickGate.setItemText(6, "")
        self.labelX = QtWidgets.QLabel(self.centralwidget)
        self.labelX.setGeometry(QtCore.QRect(100, 10, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelX.setFont(font)
        self.labelX.setObjectName("labelX")
        self.labelY = QtWidgets.QLabel(self.centralwidget)
        self.labelY.setGeometry(QtCore.QRect(390, 10, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelY.setFont(font)
        self.labelY.setObjectName("labelY")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(100, 420, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.labelResult.setFont(font)
        self.labelResult.setObjectName("labelResult")
        self.labelX_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelX_2.setGeometry(QtCore.QRect(320, 210, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelX_2.setFont(font)
        self.labelX_2.setObjectName("labelX_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.submit.clicked.connect(self.submitPressed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Logic Gate Calculations"))
        self.comboX.setItemText(0, _translate("MainWindow", "0"))
        self.comboX.setItemText(1, _translate("MainWindow", "1"))
        self.comboY.setItemText(0, _translate("MainWindow", "0"))
        self.comboY.setItemText(1, _translate("MainWindow", "1"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.comboPickGate.setItemText(0, _translate("MainWindow", "AND"))
        self.comboPickGate.setItemText(1, _translate("MainWindow", "OR"))
        self.comboPickGate.setItemText(2, _translate("MainWindow", "XOR"))
        self.comboPickGate.setItemText(3, _translate("MainWindow", "NAND"))
        self.comboPickGate.setItemText(4, _translate("MainWindow", "NOR"))
        self.comboPickGate.setItemText(5, _translate("MainWindow", "XNOR"))
        self.labelX.setText(_translate("MainWindow", "X"))
        self.labelY.setText(_translate("MainWindow", "Y"))
        self.labelResult.setText(_translate("MainWindow", "X AND Y ="))
        self.labelX_2.setText(_translate("MainWindow", "Choose gate type:"))

    def submitPressed(self):
        x = int(self.comboX.currentText())
        y = int(self.comboY.currentText())
        gate = self.comboPickGate.currentText()

        if gate == 'AND':
            _and = x and y
            self.labelResult.setText("X AND Y = " + str(_and))
        elif gate == 'OR':
            _or = x or y
            self.labelResult.setText("X OR Y = " + str(_or))
        elif gate == 'XOR':
            _xor = x ^ y
            self.labelResult.setText("X XOR Y = " + str(_xor))
        elif gate == 'NAND':
            _nand = int(not (x and y))
            self.labelResult.setText("X NAND Y = " + str(_nand))
        elif gate == 'NOR':
            _nor = int(not (x or y))
            self.labelResult.setText("X NOR Y = " + str(_nor))
        else:
            _xnor = int(x == y)
            self.labelResult.setText("X XNOR Y = " + str(_xnor))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
