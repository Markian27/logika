from PIL import Image, ImageFilter
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
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


btn_folder = QPushButton('Папка')
line_y1.addWidget(btn_folder)
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

def filter(files):
    result = []
    ext = ['jpg', 'jpeg', 'bmp', 'gif', 'jfif', 'svg', 'png']

    for file in files:
        if file.split('.')[-1] in ext:
            result.append(file)
    return result

def showFilter():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    files_and_folders = os.listdir(workdir)

    filtered_img = filter(files_and_folders)

    List.clear()
    List.addItems(filtered_img)

class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.original = None
        self.save_dir = 'Modifiled/'

    def loadImage(self, filename):
        self.filename = filename

        full_path = os.path.join(workdir, filename)


        self.original = Image.open(full_path)
    def showImage(self, path):
        lb_pic.hide()
        pixmapimg = QPixmap(path)
        w, h = lb_pic.width(), lb_pic.height()

        pixmapimg = pixmapimg.scaled(w, h, Qt.KeepAspectRatio)


        lb_pic.setPixmap(pixmapimg)
        lb_pic.show()

    def SaveAndShowImage(self):
        path = os.path.join(workdir, self.save_dir)

        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)

        image_path = os.path.join(path, self.filename)

        self.original.save(image_path)
        self.showImage(image_path)

    def doBW(self):
        self.original = self.original.convert("L")
        self.SaveAndShowImage()

    def Left(self):
        self.original = self.original.transpose(Image.ROTATE_90)
        self.SaveAndShowImage()

    def Right(self):
        self.original = self.original.transpose(Image.ROTATE_270)
        self.SaveAndShowImage()

    def do_flip(self):
        self.original = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.SaveAndShowImage()

    def Sharp(self):
        self.original = self.original.filter(ImageFilter.SHARPEN)
        self.SaveAndShowImage()




workimage = ImageProcessor()
def showChosenImage():
    filename = List.currentItem().text()
    full_path = os.path.join(workdir, filename)
    workimage.loadImage(filename)
    workimage.showImage(full_path)

window.setLayout(line_x1)

List.itemClicked.connect(showChosenImage)
btn_folder.clicked.connect(showFilter)

List.setStyleSheet("QListWidget { background-color:"
                     " #f2edc4; color: black; font-size: 16px; border-radius: 1px; }")
btn_folder.setStyleSheet("QPushButton { background-color:"
                     " #ede393; color: black; font-size: 16px; border-radius: 1px; }")
BMW.setStyleSheet("QPushButton { background-color:"
                     " #505052; color: white; font-size: 16px; border-radius: 1px; }")
left.setStyleSheet("QPushButton { background-color:"
                     " #de5252; color: black; font-size: 16px; border-radius: 1px; }")
right.setStyleSheet("QPushButton { background-color:"
                     " #de5252; color: black; font-size: 16px; border-radius: 1px; }")
sharpness.setStyleSheet("QPushButton { background-color:"
                     " #c9c7c7; color: black; font-size: 16px; border-radius: 1px; }")
mirror.setStyleSheet("QPushButton { background-color:"
                     " #8dd6d5; color: black; font-size: 16px; border-radius: 1px; }")

BMW.clicked.connect(workimage.doBW)
mirror.clicked.connect(workimage.do_flip)
sharpness.clicked.connect(workimage.Sharp)
left.clicked.connect(workimage.Left)
right.clicked.connect(workimage.Right)


window.show()
app.exec_()
