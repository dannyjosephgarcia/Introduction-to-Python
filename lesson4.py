integer_variable = 1
float_variable = 13.2
string_variable = "Hello World"
boolean_variable_true = True
boolean_variable_false = False
none_variable = None

list_variable1 = [1, 2, 3, 4, 4, 5, 69, 78]

list_variable2 = [integer_variable, float_variable, string_variable, boolean_variable_true, boolean_variable_false,
                  none_variable]
print(list_variable2)
print(type(list_variable2))

print(list_variable2)
list_variable2.append(2)
print(list_variable2)

print(list_variable2[1])
print(len(list_variable2))

# Uncommenting out the code below will cause an error. Do you know why??
# print(list_variable2[10000])
