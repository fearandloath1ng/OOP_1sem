import unittest
from unittest.mock import patch
from io import StringIO

from main import Coffee, main

class TestCoffee(unittest.TestCase):

    def test_coffee_str(self):
        coffee = Coffee("Капучино", True, "Карамель")
        self.assertEqual(str(coffee), "Капучино (с сахаром, сиропом Карамель)")

        coffee = Coffee("Латте", False)
        self.assertEqual(str(coffee), "Латте (без сахара, без сиропа)")

    def test_coffee_with_sugar(self):
        coffee = Coffee("Эспрессо", True)
        self.assertTrue(coffee.with_sugar)

    def test_coffee_without_sugar(self):
        coffee = Coffee("Эспрессо", False)
        self.assertFalse(coffee.with_sugar)

    @patch('builtins.input', side_effect=['1', 'да', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Ваш заказ: Капучино (с сахаром, без сиропа)", output)

    @patch('builtins.input', side_effect=['4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_invalid_coffee_choice(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Неверный выбор. Попробуйте снова.", output)

    @patch('builtins.input', side_effect=['1', 'да', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_with_syrup(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Ваш заказ: Капучино (с сахаром, сиропом Шоколад)", output)

if __name__ == '__main__':
    unittest.main()
