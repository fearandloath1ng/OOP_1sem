from person import Person

class Teacher(Person):
    def __init__(self, surname, name, birth_date, subjects):
        super().__init__(surname, name, birth_date)
        self.subjects = subjects

    def is_valid_teacher(self):
        return 27 <= self.age() <= 70

    def __str__(self):
        return f'Teacher: {self.surname} {self.name}, Subjects: {", ".join(self.subjects)}'