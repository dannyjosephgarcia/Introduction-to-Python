integer_variable = 1
float_variable = 13.2
string_variable = "Hello World"
boolean_variable_true = True
boolean_variable_false = False
none_variable = None

# Mutable: Any 'object' that can be altered
# Immutable: Any 'object' that cannot be altered
# Time complexity: The amount of RELATIVE time it takes for an operation to execute

set_variable = {2, 2}
duplicate_list_variable = [1, 2, 1, 2]
print(type(set_variable))
print(duplicate_list_variable)
print(set_variable)

list_variable = [1, 2, 3, 4]  # It takes linear time to find an element
if 2 in list_variable:
    print("Yes")

set_variable_1 = {1, 2}  # An element can be found in a set in constant time
set_variable_1.add(3)
print(set_variable_1)

# The below line will cause an error
# print(set_variable[1])
