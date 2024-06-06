integer_variable = 1
float_variable = 13.2
string_variable = "Hello World"
boolean_variable_true = True
boolean_variable_false = False
none_variable = None

# Mutable: Any 'object' that can be altered
# Immutable: Any 'object' that cannot be altered

tuple_datastructure = (1, 2)
list_variable = [1, 3]
# The below lines will cause errors since tuples are immutable
# tuple_datastructure.append(3)
# tuple_datastructure.remove(3)
# tuple_datastructure[1] = 5

print(list_variable)
list_variable[1] = 5
print(list_variable)

list_data_structure = list(tuple_datastructure)
print(type(list_data_structure))
list_data_structure.append(3)
tuple_datastructure = tuple(list_data_structure)

list_variable1 = [1, 2]
list_variable2 = [3, 4]
combined_list = list_variable1 + list_variable2
print(combined_list)

# Tuple workarounds via concatenation
tuple_variable_1 = (1, 2)
tuple_variable_2 = (3, 4)
combined_tuple = tuple_variable_1[:1] + (0,) + tuple_variable_2[:1]
print(combined_tuple)
