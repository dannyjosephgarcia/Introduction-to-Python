# Object-Oriented Programming
# In Python, classes are objects that store methods (functions)
# In Python, classes also store attributes
from time import time
import numpy as np


class NumberManipulation:
    def __init__(self, base_variable):
        self.base_integer = base_variable

    def raise_to_power(self, power_variable):
        """
        Function raises a number to a power
        :param power_variable: The exponent
        :return: python int, the result of base raised to the power variable
        """
        result = self.base_integer ** power_variable
        return result

    def add_number_to_integer_attribute(self, addition_number):
        result = self.base_integer + addition_number
        return result


class Dummy:
    pass


class Dummy2:
    pass


# ==================================================================================================================== #
if __name__ == "__main__":
    number_manipulations = NumberManipulation(3)
    test_list = [1, 2]
    print(int(time()))
    print(np.average(test_list))
