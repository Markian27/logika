from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel,
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget,  QListWidgetItem, QFormLayout,
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json

app = QApplication([])
window = QWidget()

line1 = QVBoxLayout()
line2 = QVBoxLayout()

line_x1 = QHBoxLayout()
line_x2 = QHBoxLayout()
layout_notes = QHBoxLayout()

layout_notes.addLayout(line1, stretch=2)
layout_notes.addLayout(line2, stretch=1)

file_text = QTextEdit()
line1.addWidget(file_text)

id_notes = QLabel('Список заміток ')
line2.addWidget(id_notes)

lmt_notes = QLineEdit()
line2.addWidget(lmt_notes)

lst_notes = QLabel('Список тегів ')



btn_create_notes = QPushButton('Створити замітку')
btn_delete_notes = QPushButton('Видалити замітку')
btn_save_notes = QPushButton('Зберегти замітку')
btn_add_notes = QPushButton('Додати до замітки')
btn_unpin_notes = QPushButton('Відкріпити замітку')
btn_search_notes = QPushButton('Шукати замітку за тегом')


with open("notes.json", 'r', encoding="utf-8") as file:
    notes = json.load(file)



window.setLayout(layout_notes)
window.setLayout(line1)
window.setLayout(line2)

window.show()
app.exec_()