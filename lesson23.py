import unittest

def add_two_numbers(num1, num2):
    """
    Function adds two numbers
    :param num1: The first number
    :param num2: The second number
    :return: python int, the sum
    """
    try:
        result = num1 + num2
        return result
    except Exception as e:
        print(str(e))
        raise TypeError("One of the numbers is not of the correct datatype")


class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers_happy(self):
        result = add_two_numbers(1, 2)
        self.assertEqual(3, result)

    def test_add_two_numbers_invalid_character(self):
        with self.assertRaises(TypeError):
            add_two_numbers(1, '2')


if __name__ == "__main__":
    unittest.main()
