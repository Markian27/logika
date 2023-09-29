import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel,
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget,  QListWidgetItem, QFormLayout,
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)


def write_file():
    with open('notes.json', 'w', encoding='utf8') as file:
        json.dump(notes, file, ensure_ascii=False, sort_keys=True, indent=4)

app = QApplication([])
window = QWidget()

line1 = QVBoxLayout()
line2 = QVBoxLayout()

layout_notes = QHBoxLayout()

layout_notes.addLayout(line1, stretch=2)
layout_notes.addLayout(line2, stretch=1)


line_x0 = QHBoxLayout()
line_x1 = QHBoxLayout()
line_x2 = QHBoxLayout()
line_x3 = QHBoxLayout()
line_x4 = QHBoxLayout()
line_x5 = QHBoxLayout()
line_x6 = QHBoxLayout()
line_x7 = QHBoxLayout()
line_x8 = QHBoxLayout()
liner = [line_x0, line_x1, line_x2, line_x3, line_x4, line_x5, line_x6, line_x7, line_x8]
for l in liner:
    line2.addLayout(l)


file_text = QTextEdit()
line1.addWidget(file_text)

id_notes = QLabel('Список заміток ')
line_x0.addWidget(id_notes)

lst_notes = QListWidget()
line_x1.addWidget(lst_notes)


btn_create_notes = QPushButton('Створити замітку')
line_x2.addWidget(btn_create_notes)
btn_delete_notes = QPushButton('Видалити замітку')
line_x2.addWidget(btn_delete_notes)
btn_save_notes = QPushButton('Зберегти замітку')
line_x3.addWidget(btn_save_notes)


lst_tags = QLabel('Список тегів ')
line_x4.addWidget(lst_tags)

tag_notes = QListWidget()
line_x5.addWidget(tag_notes)

line_edit = QLineEdit()
line_x6.addWidget(line_edit)

btn_add_notes = QPushButton('Додати до замітки')
line_x8.addWidget(btn_add_notes)
btn_unpin_notes = QPushButton('Відкріпити замітку')
line_x8.addWidget(btn_unpin_notes)
btn_search_notes = QPushButton('Шукати замітку за тегом')
line_x7.addWidget(btn_search_notes)

def show_notes():
    key = lst_notes.selectedItems()[0].text()
    file_text.setText(notes[key]['текст'])

    #lst_tags.clear()
    #lst_tags.addItems(notes[key]['теги'])

def add_note():
    note_name, ok = QInputDialog.getText(window, 'Додати замітку', 'Назва замітки')
    if note_name and ok:
        lst_notes.addItem(note_name)
        notes[note_name] = {'текст': '', 'теги': ''}

        write_file()

btn_create_notes.clicked.connect(add_note)

def del_note():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        del notes[key]

    file_text.clear()
    lst_tags.clear()
    lst_notes.clear()
    lst_notes.addItems(notes)

    write_file()

btn_delete_notes.clicked.connect(del_note)

def save_notes():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()

        notes[key]['текст'] = file_text.toPlainText()

        write_file()

btn_save_notes.clicked.connect(save_notes)

with open("notes.json", 'r', encoding="utf8") as file:
    notes = json.load(file)


lst_notes.addItems(notes)
lst_notes.clicked.connect(show_notes)



window.setLayout(layout_notes)
window.setLayout(line1)
window.setLayout(line2)
window.setLayout(line_x1)
window.setLayout(line_x2)

window.show()
app.exec_()
