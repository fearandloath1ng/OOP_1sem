from person import Person

class Student(Person):
    def __init__(self, surname, name, birth_date, class_level):
        super().__init__(surname, name, birth_date)
        self.class_level = class_level
        self.teachers = []
        self.grades = {}

    def add_teacher(self, teacher):
        if self.age() < 18 and teacher not in self.teachers:
            self.teachers.append(teacher)

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def __str__(self):
        return f'Student: {self.surname} {self.name}, Class: {self.class_level}'
