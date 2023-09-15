class Student():
    def __init__(self, surname, name, qreat):
        self.surname = surname
        self.name = name
        self.qreat = qreat

student = []

with open("sts.txt", encoding="utf-8") as file:
    for line in file:
        data = line.split(" ")
        jd = Student(data[0], data[1], int(data[2]))
        student.append(jd)

for s in student:
    if s.qreat == 5:
        print(s.surname, s.name, 'Оцінка:', s.qreat)


