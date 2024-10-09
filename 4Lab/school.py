class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self, student):
        if student.age() >= 18:
            print(f'Ученик {student} слишком стар.')
        else:
            self.students.append(student)

    def add_teacher(self, teacher):
        if teacher.is_valid_teacher():
            self.teachers.append(teacher)
        else:
            print(f'Учитель {teacher} не имеет права учить.')

    def assign_teachers_to_students(self):
        for student in self.students:
            subjects = ['Математика', 'Русский язык', 'Науки о природе']
            if student.class_level in ['1', '2', '3', '4', '5', '6']:
                for teacher in self.teachers:
                    if any(subj in teacher.subjects for subj in subjects):
                        student.add_teacher(teacher)
            elif student.class_level in ['7', '8', '9', '10', '11']:
                extended_subjects = subjects + ['Физика', 'Химия', 'Информатика', 'Биология']
                for teacher in self.teachers:
                    if any(subj in teacher.subjects for subj in extended_subjects):
                        student.add_teacher(teacher)

    def add_grade_to_student(self, student, subject, grade):
        if student in self.students:
            student.add_grade(subject, grade)
        else:
            print(f'Студент {student} не найден в системе.')

    def generate_report(self):
        with open('class_report.txt', 'w') as f:
            for student in self.students:
                f.write(str(student) + "\n")
                for teacher in student.teachers:
                    f.write(f"  -> {teacher}\n")
                for subject, grades in student.grades.items():
                    f.write(f"    {subject} Оценки: {', '.join(map(str, grades))}\n")