integer_variable = 1
float_variable = 13.2
string_variable = "Hello World"
boolean_variable_true = True
boolean_variable_false = False
none_variable = None

list_variable1 = [integer_variable, float_variable, string_variable, boolean_variable_true, boolean_variable_false,
                  none_variable]
print(list_variable1[1])

print(list_variable1.index(float_variable))

print(list_variable1)
list_variable1.remove(none_variable)
print(list_variable1)

numbers_list = [1, 2, 3, 4, 5]
print(max(numbers_list))
print(min(numbers_list))
print(sum(numbers_list))
print(sorted(numbers_list, reverse=True))
print(sorted(numbers_list, reverse=False))
