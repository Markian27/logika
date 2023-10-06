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

btn_add_tag = QPushButton('Додати тег')
line_x8.addWidget(btn_add_tag)
btn_unpin_tag = QPushButton('Відкріпити тег')
line_x8.addWidget(btn_unpin_tag)
btn_search_tag = QPushButton('Шукати за тегом')
line_x7.addWidget(btn_search_tag)

def show_notes():
    key = lst_notes.selectedItems()[0].text()
    file_text.setText(notes[key]['текст'])

    tag_notes.clear()
    tag_notes.addItems(notes[key]['теги'])

def add_note():
    note_name, ok = QInputDialog.getText(window, 'Додати замітку', 'Назва замітки')
    if note_name and ok:
        lst_notes.addItem(note_name)
        notes[note_name] = {'текст': '', 'теги': ['']}
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

def save_notes():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()

        notes[key]['текст'] = file_text.toPlainText()
        write_file()

def add_tag():
    key = lst_notes.currentItem().text()
    tag = line_edit.text()

    if tag:
        notes[key]['теги'].append(tag)
        tag_notes.addItem(tag)
        line_edit.clear()
        write_file()

def del_tag():
    key = lst_notes.currentItem().text()
    tag = tag_notes.currentItem()

    if tag:
        notes[key]['теги'].remove(tag.text())
        tag_notes.takeItem(tag_notes.row(tag))
        write_file()

def search_tag():
    tag = line_edit.text()

    if 'Шукати за тегом' == btn_search_tag.text():
        filter_notes = {}

        for key in notes:
            if tag in notes[key]['теги']:
                filter_notes[key] = notes[key]
        btn_search_tag.setText('Скинути пошук')
        lst_notes.clear()
        lst_notes.addItems(filter_notes)
        lst_tags.clear()
        file_text.clear()

    elif 'Скинути пошук' == btn_search_tag.text():
        btn_search_tag.setText('Шукати за тегом')

        lst_notes.clear()
        lst_notes.addItems(notes)
        lst_tags.clear()
        file_text.clear()

btn_add_tag.clicked.connect(add_tag)
btn_search_tag.clicked.connect(search_tag)
btn_unpin_tag.clicked.connect(del_tag)

btn_delete_notes.clicked.connect(del_note)


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
