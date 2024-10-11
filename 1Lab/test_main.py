import unittest
from unittest.mock import patch
from io import StringIO

from main import Question, get_grade, main

class TestQuestion(unittest.TestCase):

    def setUp(self):
        self.question = Question("Что такое класс?", "Шаблон для создания объектов", "Объект", "Интерфейс", "Модуль", 1)

    def test_get_question(self):
        self.assertEqual(self.question.get_question(), "Что такое класс?")

    def test_get_answers(self):
        self.assertEqual(self.question.get_answers(), ["Шаблон для создания объектов", "Объект", "Интерфейс", "Модуль"])

    def test_is_correct(self):
        self.assertTrue(self.question.is_correct(1))
        self.assertFalse(self.question.is_correct(2))

class TestGetGrade(unittest.TestCase):

    def test_get_grade(self):
        self.assertEqual(get_grade(5), "Отлично")
        self.assertEqual(get_grade(4), "Хорошо")
        self.assertEqual(get_grade(3), "Удовлетворительно")
        self.assertEqual(get_grade(2), "Неудовлетворительно")

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '1', '2', '3', '4', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Результаты:", output)

if __name__ == '__main__':
    unittest.main()
