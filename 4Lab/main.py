from student import Student
from teacher import Teacher
from school import School

# Пример
school = School()

student1 = Student('Сидоров', 'Сидор', '2009-02-20', '9')
student2 = Student('Лебедев', 'Алексей', '2010-03-22', '8')

teacher1 = Teacher('Иванов', 'Иван', '1990-01-01', ['Математика'])
teacher2 = Teacher('Петров', 'Петр', '1985-06-15', ['Русский язык'])
teacher3 = Teacher('Константинов', 'Константин', '1987-07-11', ['Науки о природе'])
teacher4 = Teacher('Павлов', 'Павел', '1970-01-01', ['Химия'])
teacher5 = Teacher('Никитин', 'Никита', '1965-02-21', ['Биология', 'Химия'])
teacher6 = Teacher('Соколова', 'Ольга', '1977-03-31', ['Физика', 'Информатика'])
teacher7 = Teacher('Петрова', 'Мария', '1979-11-01', ['Информатика'])

school.add_teacher(teacher1)
school.add_teacher(teacher2)
school.add_teacher(teacher3)
school.add_teacher(teacher4)
school.add_teacher(teacher5)
school.add_teacher(teacher6)
school.add_teacher(teacher7)

school.add_student(student1)
school.add_student(student2)

school.assign_teachers_to_students()

school.add_grade_to_student(student1, "Математика", 5)
school.add_grade_to_student(student2, "Физика", 4)
school.add_grade_to_student(student1, "Математика", 2)
school.add_grade_to_student(student2, "Информатика", 5)

school.generate_report()
