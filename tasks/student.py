"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: int
    average_score: float

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other

    def __lt__(self, other):
        return self.average_score < other

    def __gt__(self, other):
        return self.average_score > other

    def __ne__(self, other):
        return self.average_score != other

    def __le__(self, other):
        return self.average_score <= other

    def __ge__(self, other):
        return self.average_score >= other

    def __repr__(self):
        return "{} {} {} {}".format(self.surname, self.name, self.group, self.average_score)


student1 = Student("Nadya", "Kiryanovich", 6, 7.2)
student2 = Student("Kirill", "Ivanov", 6, 5.6)
student3 = Student("Masha", "Zhukovskaja", 6, 9.8)
student4 = Student("Dmitrij", "Orlov", 6, 4.7)
student5 = Student("Petya", "Shashlyk", 6, 8.6)

student_list = [student1, student2, student3, student4, student5]

print(sorted(student_list))

print(sorted(student_list, reverse=True))

for a in student_list:
    if a.average_score > 5:
        print(a)
