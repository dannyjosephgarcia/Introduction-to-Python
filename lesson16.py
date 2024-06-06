# The syntax for a function is as follows...
# 1. The keyword 'def'
# 2. The function name given in snake_case
# 3. open and closed parentheses ()
# 4. A colon

def square_number(integer_variable):
    result = integer_variable ** 2
    return result


print(square_number(2))


def raise_to_power(base_integer, power_variable):
    """
    Function raises a number to a power
    :param base_integer: The base integer
    :param power_variable: The exponent
    :return: python int, the result of base raised to the power variable
    """
    result = base_integer ** power_variable
    return result


print(raise_to_power(3, 3))


def multi_outputs(base_integer, power_variable):
    result = base_integer ** power_variable
    dummy_number = 2
    return result, dummy_number


result, dummy_number = multi_outputs(3, 3)
print(result)
print(dummy_number)
