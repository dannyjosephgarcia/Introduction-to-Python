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
    finally:
        return 3


if __name__ == "__main__":
    print(add_two_numbers(2, 2))
    print(add_two_numbers(1, '2'))
