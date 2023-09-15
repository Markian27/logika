from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
window = QWidget()

text = QLabel("Натисни")
winner = QLabel("?")
btn = QPushButton(" ")

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(btn, alignment=Qt.AlignCenter)
def win():
    ran = randint(1, 100)
    winner.setText(str(ran))

btn.clicked.connect(win)


window.setLayout(line)

window.show()
app.exec_()