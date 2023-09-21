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
        pt = len(student)
suma = 0
ss = 0
for s in student:
    if s.qreat == 5:
        print(s.surname, s.name, 'Оцінка:', s.qreat)
        suma += 5
        ss += 1
    if s.qreat == 4:
        suma += 4
        ss += 1
    if s.qreat == 3:
        suma += 3
        ss += 1
    if s.qreat == 2:
        suma += 2
        ss += 1
    medium = round(suma / ss, 1)

print('Загальна кількість балів:', suma)
print('Кількість студентів:', pt)
print('Середнє арифметичне:', medium)

