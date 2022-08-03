from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TicTacToe ")
        self.setGeometry(100, 100, 300, 500)
        self.initUI()
        self.show()
    
    def initUI(self):
        self.turn = 0
        self.times = 0

        self.button_list = []

        for i in range(3):
            row = []
            for j in range(3):
                row.append((QPushButton(self)))
            self.button_list.append(row)

        x = 90
        y = 90

        for i in range(3):
            for j in range(3):
                self.button_list[i][j].setGeometry(x*i + 20, y*j + 20,80,80)
                self.button_list[i][j].setFont(QFont(QFont('Times', 17)))
                self.button_list[i][j].clicked.connect(self.markXO)

        self.label = QLabel(self)
        self.label.setGeometry(20, 300, 260, 60)
        self.label.setStyleSheet("QLabel"
								"{"
								"border : 3px solid black;"
								"background : white;"
								"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Times", 15))

        reset = QPushButton("Reset Game", self)
        reset.setGeometry(50, 380, 200, 50)
        reset.clicked.connect(self.reset_button)

    def reset_button(self):
        self.turn = 0
        self.times = 0

        self.label.setText("")

        for buttons in self.button_list:
            for button in buttons:
                button.setEnabled(True)
                button.setText("")
    def markXO(self):
        self.times +=1

        button = self.sender()
        button.setEnabled(False)

        if self.turn == 1:
            button.setText("O")
            self.turn = 0
        else:
            button.setText("X")
            self.turn = 1

        win = self.win_check()

        text = ""

        if win == True:
            if self.turn == 0:
                text = "O Wins"

            else:
                text = "X wins"

            for i in self.button_list:
                for j in i:
                    j.setEnabled(False)
        
        elif self.times == 9:
            text = "Draw"

        self.label.setText(text)

                

    def win_check(self):
        
        for i in range(3):
            if self.button_list[0][i].text() == self.button_list[1][i].text()and self.button_list[0][i].text() == self.button_list[2][i].text() and self.button_list[0][i].text() != "":
                return True

            if self.button_list[i][0].text() == self.button_list[i][1].text()and self.button_list[i][0].text() == self.button_list[i][2].text() and self.button_list[i][0].text() != "":
                return True

        if self.button_list[0][0].text() == self.button_list[1][1].text()and self.button_list[0][0].text() == self.button_list[2][2].text() and self.button_list[0][0].text() != "":
                return True

        if self.button_list[0][2].text() == self.button_list[1][1].text()and self.button_list[1][1].text() == self.button_list[2][0].text() and self.button_list[0][2].text() != "":
                return True

        return False


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())

