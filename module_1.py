from multiply_two_numbers import MultiplyTwoNumbers


class AddTwoNumbers:
    @staticmethod
    def add_two_numbers(num1):
        """
        Adds the two numbers provided
        :param num1: The first number added
        :return: python int
        """
        try:
            num2 = MultiplyTwoNumbers().multiply_two_numbers(1, 2)
            if num2 <= 2:
                result = num1 + num2
                return result
            else:
                result = num1 + (2 * num2)
                return result
        except Exception as e:
            raise ValueError("One of the inputs received was of the wrong datatype")


if __name__ == "__main__":
    print(AddTwoNumbers().add_two_numbers(2))
