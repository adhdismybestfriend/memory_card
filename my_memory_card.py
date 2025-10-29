#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QButtonGroup
from random import shuffle, randint

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question("Siapa presiden ke 3", "BJ Habibie", "Munir", "Soekarno", "Jusuf Kalla"))
question_list.append(Question("Pekerjaan apa yang romantis", "Pelukis", "Dokter", "Buruh Pabrik", "Guru"))
question_list.append(Question("Kapan tanggal kemerdekaan indonesia", "17 Agustus", "28 Mei", "27 Juni", "18 Agustus"))
app = QApplication([])
window = QWidget()
#window.resize(700, 400)
window.setWindowTitle('Memory Card')

question = QLabel('Ayam berkokok di jam berapa?')
answer_button = QPushButton('Jawab')

rtbn_1 = QRadioButton('Option 1')
rtbn_2 = QRadioButton('Option 2')
rtbn_3 = QRadioButton('Option 3')
rtbn_4 = QRadioButton('Option 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rtbn_1)
RadioGroup.addButton(rtbn_2)
RadioGroup.addButton(rtbn_3)
RadioGroup.addButton(rtbn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rtbn_1)
layout_ans2.addWidget(rtbn_2)
layout_ans3.addWidget(rtbn_3)
layout_ans3.addWidget(rtbn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox = QGroupBox('Opsi Jawaban')
RadioGroupBox.setLayout(layout_ans1)

hasil = QLabel('Benar')
hasil_benar = QLabel('Hasil')
layout_hasil = QVBoxLayout()
layout_hasil.addWidget(hasil)
layout_hasil.addWidget(hasil_benar)
AnswerGroupBox = QGroupBox('Hasil')
lb_Result = QLabel("Were you correct or not?")
lb_Correct = QLabel('The answer will be there!')
AnswerGroupBox.setLayout(layout_hasil)

layout_h1 = QHBoxLayout()
layout_h2 = QHBoxLayout()
layout_h3 = QHBoxLayout()
layout_h1.addWidget(question, alignment = Qt.AlignCenter)
layout_h2.addWidget(RadioGroupBox)
layout_h2.addWidget(AnswerGroupBox)
AnswerGroupBox.hide()
layout_h3.addWidget(answer_button, stretch = 2)

main_layout = QVBoxLayout()
main_layout.addLayout(layout_h1)
main_layout.addLayout(layout_h2)
main_layout.addLayout(layout_h3, stretch = 1)
main_layout.setSpacing(15)
window.setLayout(main_layout)

def show_result():
    AnswerGroupBox.show()
    RadioGroupBox.hide()
    answer_button.setText('Pertanyaan Selanjutnya')

def show_question():
    AnswerGroupBox.hide()
    RadioGroupBox.show()
    answer_button.setText('Jawab')
    RadioGroup.setExclusive(False)
    rtbn_1.setChecked(False)
    rtbn_2.setChecked(False)
    rtbn_3.setChecked(False)
    rtbn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rtbn_1, rtbn_2, rtbn_3, rtbn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()
def start_test():
    if answer_button.text() == 'Jawab':
        check_answer()
    else:
        next_question()

def check_answer():
    if answers[0].isChecked():
        show_correct("BENAR")
        window.score += 1
        print("Statistik\n-Total Question:", window.total, "\n-Total Right Answer:", window.score)
        print('Rating:', (window.score/window.total)*100, '%')
    
    else:
        if answers[1].isChecked()or answers[2].isChecked()or answers[3].isChecked():
            show_correct("Jawaban Salah")
            print('Rating:', (window.score/window.total)*100, '%')

def next_question():
    window.total += 1
    print("Statistik\n-Total Question:", window.total, "\n-Total Right Answer:", window.score)
    cur_question = randint(0,len(question_list)-1)
    q = question_list[cur_question]
    ask(q)
            

answer_button.clicked.connect(start_test)
window.score = 0
window.total = 0
next_question()
window.show()
app.exec()