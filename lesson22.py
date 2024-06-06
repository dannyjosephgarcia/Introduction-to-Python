import timeit


def function_time(func):
    def wrapper(num1, num2):
        start_time = timeit.default_timer()
        result = func(num1, num2)
        time_of_function = timeit.default_timer() - start_time
        print(f"The time of the {func.__name__} function is {time_of_function}")
        return result

    return wrapper


@function_time
def add_two_numbers(num1, num2):
    result = num1 + num2
    return result


@function_time
def multiply_two_numbers(num1, num2):
    result = num1 * num2
    return result


if __name__ == "__main__":
    print(add_two_numbers(2, 2))
    print(multiply_two_numbers(2, 3))
