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

layout_notes = QHBoxLayout()

layout_notes.addLayout(line1, stretch=2)
layout_notes.addLayout(line2, stretch=1)

line_x1 = QHBoxLayout()
line_x2 = QHBoxLayout()
line2.addLayout(line_x1)
line2.addLayout(line_x2)


file_text = QTextEdit()
line1.addWidget(file_text)

id_notes = QLabel('Список заміток ')
line2.addWidget(id_notes)

lst_notes = QListWidget()
line2.addWidget(lst_notes)


btn_create_notes = QPushButton('Створити замітку')
line_x1.addWidget(btn_create_notes)
btn_delete_notes = QPushButton('Видалити замітку')
line_x1.addWidget(btn_delete_notes)
btn_save_notes = QPushButton('Зберегти замітку')
line2.addWidget(btn_save_notes)


lmt_notes = QLabel('Список тегів ')
line2.addWidget(lmt_notes)

lpt_notes = QListWidget()
line2.addWidget(lpt_notes)

btn_add_notes = QPushButton('Додати до замітки')
line_x2.addWidget(btn_add_notes)
btn_unpin_notes = QPushButton('Відкріпити замітку')
line_x2.addWidget(btn_unpin_notes)
btn_search_notes = QPushButton('Шукати замітку за тегом')
line2.addWidget(btn_search_notes)

def show_notes():
    key = lst_notes.selectedItems()[0].text()
    file_text.setText(notes[key]['текст'])


with open("notes.json", 'r', encoding="utf-8") as file:
    notes = json.load(file)

#lst_notes.addItem(notes)

window.setLayout(layout_notes)
window.setLayout(line1)
window.setLayout(line2)
window.setLayout(line_x1)
window.setLayout(line_x2)

window.show()
app.exec_()
