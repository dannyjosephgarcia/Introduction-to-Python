import unittest
from module_1 import AddTwoNumbers
from multiply_two_numbers import MultiplyTwoNumbers
from unittest.mock import patch


class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.add_two_numbers = AddTwoNumbers

    def test_add_two_numbers_less_than_two(self):
        result = self.add_two_numbers.add_two_numbers(2)
        self.assertEqual(4, result)

    @patch.object(MultiplyTwoNumbers, 'multiply_two_numbers', return_value=3)
    def test_add_two_numbers_greater_than_two(self, mock_two_numbers_product):
        result = self.add_two_numbers.add_two_numbers(2)
        self.assertEqual(8, result)


if __name__ == "__main__":
    unittest.main()
