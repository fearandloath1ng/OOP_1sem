import unittest

from student import Student
from teacher import Teacher
from school import School

class TestSchoolSystem(unittest.TestCase):

    def setUp(self):
        self.student = Student('Сидоров', 'Сидор', '2009-02-20', '9')
        self.teacher = Teacher('Иванов', 'Иван', '1990-01-01', ['Математика'])
        self.school = School()

    def test_person_age(self):
        self.assertGreater(self.student.age(), 0, "Age should be greater than 0")

    def test_student_repr(self):
        self.assertEqual(str(self.student), "Student: Сидоров Сидор, Class: 9")

    def test_teacher_validity(self):
        self.assertTrue(self.teacher.is_valid_teacher(), "Учитель должен проходить по требованиям")

    def test_add_teacher_to_student(self):
        self.school.add_teacher(self.teacher)
        self.student.add_teacher(self.teacher)
        self.assertIn(self.teacher, self.student.teachers, "Учитель должен быть в списке учителей")

    def test_add_grade(self):
        self.student.add_grade("Математика", 5)
        self.student.add_grade("Математика", 4)
        self.assertIn(5, self.student.grades['Математика'], "Оценка 5 должна быть в журнале")
        self.assertIn(4, self.student.grades['Математика'], "Оценка 4 должна быть в журнале")

    def test_add_student(self):
        self.school.add_student(self.student)
        self.assertIn(self.student, self.school.students, "Студент не должен быть в школьном списке")

if __name__ == '__main__':
    unittest.main()
