#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QWidget, QPushButton, QButtonGroup, QGroupBox, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout
from random import shuffle
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions = []
questions.append(Question('Вопрос', 'ответ', 'ответ2', 'ответ3', 'ответ4'))
questions.append(Question('Вопрос2', 'ответ_1', 'ответ_2', 'ответ_3', 'ответ_4'))
questions.append(Question('Вопрос3', 'ответ_правильный', 'ответ2_неправильный', 'ответ3_неправильный', 'ответ4_неправильный'))
#функции
def show_result():
    RadioGroupBox.hide()
    answer_group.show()
    button.setText('Следующий вопрос')    
def show_question():
    RadioGroupBox.show()
    answer_group.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
def start_test():
    if button.text() == 'Ответить':
        check_answer()
    else:
        show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
    else:
        show_correct('Неправильно')
    show_result()
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lbl_right.setText(q.right_answer)
    show_question()
def show_correct(res):
    lbl_res.setText(res)
    show_result()
def next_question():
    main_win.number += 1
    if main_win.number > len(questions) - 1:
        main_win.number = 0
    ask(questions[main_win.number])
def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.number = -1
main_win.resize(500, 300)
main_win.setWindowTitle('Memory Card')
#создание виджетов главного окна
RadioGroupBox = QGroupBox('Варианты ответов')
question = QLabel('Какой национальности не существует?')
btn_answer1 = QRadioButton('Энцы')
btn_answer2 = QRadioButton('Смурфы')
btn_answer3 = QRadioButton('Чулымцы')
btn_answer4 = QRadioButton('Алеуты')
button = QPushButton('Ответить')
answer_group = QGroupBox()
lbl_res = QLabel('Правильно\неправильно')
lbl_right = QLabel('Смурфы')
answer_layout = QVBoxLayout()
answer_layout.addWidget(lbl_res, alignment = Qt.AlignLeft)
answer_layout.addWidget(lbl_right, alignment = Qt.AlignCenter)
answer_group.setLayout(answer_layout)
answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
#сброс
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)
#расположение виджетов по лэйаутам
layout_main = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(btn_answer1)
layout_ans2.addWidget(btn_answer2)
layout_ans3.addWidget(btn_answer3)
layout_ans3.addWidget(btn_answer4)
h1.addWidget(question, alignment = Qt.AlignCenter)

h2.addStretch(1)
h2.addWidget(button, stretch = 1)
h2.addStretch(1)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
layout_main.addLayout(h1)
layout_main.addWidget(RadioGroupBox)
layout_main.addWidget(answer_group)
layout_main.addLayout(h2)
#отображение окна приложения
main_win.setLayout(layout_main)
main_win.show()
answer_group.hide()
button.clicked.connect(click_ok)
app.exec_()