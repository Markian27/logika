from PIL import Image, ImageFilter
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel,
    QListWidget, QPushButton, QLineEdit, QFileDialog, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget,  QListWidgetItem, QFormLayout,
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox, QMainWindow, QShortcut)

app = QApplication([])
window = QWidget()

line_x1 = QHBoxLayout()
line_x2 = QHBoxLayout()

line_y1 = QVBoxLayout()
line_y2 = QVBoxLayout()

lb_pic = QLabel('Картинка')
line_y2.addWidget(lb_pic)

line_y2.addLayout(line_x2)
line_x1.addLayout(line_y1, stretch=1)
line_x1.addLayout(line_y2, stretch=4)


folder = QPushButton('Папка')
line_y1.addWidget(folder)
left = QPushButton('Вліво')
line_x2.addWidget(left)
right = QPushButton('Вправо')
line_x2.addWidget(right)
mirror = QPushButton('Дзеркало')
line_x2.addWidget(mirror)
sharpness = QPushButton('Різкість')
line_x2.addWidget(sharpness)
BMW = QPushButton('Ч/Б')
line_x2.addWidget(BMW)

List = QListWidget()
line_y1.addWidget(List)


wordir = QFileDialog.getExistingDirectory()
files_and_folders = os.listdir(wordir)

def filter(files):
    result = []
    ext = ['jpg', 'jpeg', 'bmp', 'gif', 'jfif', 'svg', 'png']

    for file in files:
        if file.split('.')[-1] in ext:
            result.append(file)
    return result

print(filter(files_and_folders))

window.setLayout(line_x1)

window.setStyleSheet("QListWidget { background-color:"
                     " #f2edc4; color: black; font-size: 16px; border-radius: 1px; }")


window.show()
app.exec_()
