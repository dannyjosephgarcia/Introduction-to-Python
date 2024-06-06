integer_variable = 1
float_variable = 13.2
string_variable = "Hello World"
boolean_variable_true = True
boolean_variable_false = False
none_variable = None

# Mutable: Any 'object' that can be altered
# Immutable: Any 'object' that cannot be altered
# Time complexity: The amount of RELATIVE time it takes for an operation to execute

dict_variable = {'key1': 'value1', 'key2': 'value2'}

# The below code will cause an error since keys of a dictionary must be immutable
# dict_variable = {'key1': 'value1', [1]: 'value2'}

for key in dict_variable.keys():
    print(key)

for value in dict_variable.values():
    print(value)

for key, value in dict_variable.items():
    print(key)
    print(value)

print(dict_variable['key1'])

dict_variable1 = {}
dict_variable1['key1'] = 2
print(dict_variable1)

dict_variable1['key1'] = 3
print(dict_variable1)

dict_variable2 = {'key1': [1, 2, 3], 'key2': {'key1': 42}}
