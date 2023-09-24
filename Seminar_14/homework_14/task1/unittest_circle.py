import io
import unittest
from unittest.mock import patch
from circle import Circle, RadiusError


class TestCircle(unittest.TestCase):
    def setUp(self) -> Circle:
        self.circle_1 = Circle(5)
        self.circle_2 = Circle(10)
        self.circle_3 = Circle(5)

    def test_calc_len_1(self):
        self.assertEqual(self.circle_1.calc_len(), 31.41592653589793)

    def test_calc_len_2(self):
        self.assertEqual(self.circle_2.calc_len(), 62.83185307179586)

    def test_calc_area_1(self):
        self.assertEqual(self.circle_1.calc_area(), 78.53981633974483)

    def test_calc_area_2(self):
        self.assertEqual(self.circle_2.calc_area(), 314.1592653589793)

    def test_str_1(self):
        self.assertEqual(self.circle_1.__str__(), 'Круг с радиусом 5')

    def test_str_2(self):
        self.assertEqual(self.circle_2.__str__(), 'Круг с радиусом 10')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warning_false(self, mock_stdout):
        with self.assertRaises(RadiusError):
            Circle(0)
            self.assertEqual(mock_stdout.getvalue(),
            'Значение радиуса должно быть положительное.Вы вводите: 0')

    def test_eq(self):
        self.assertTrue(self.circle_1 == self.circle_3)
        self.assertFalse(self.circle_1 == self.circle_2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
