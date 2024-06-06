integer_variable = 1
float_variable = 13.2
string_variable = "Hello World"
boolean_variable_true = True
boolean_variable_false = False
none_variable = None

# Feel free to play around with typecasting below!!!
test_variable = "None"
print(type(test_variable))
print(type(integer_variable))

transformed_variable = str(integer_variable)
print(type(transformed_variable))
print(transformed_variable)

transformed_variable2 = int(float_variable)
print(type(transformed_variable2))
print(transformed_variable2)

transformed_variable3 = float_variable(integer_variable)
print(type(transformed_variable3))
print(transformed_variable3)

transformed_variable4 = str(none_variable)
print(type(transformed_variable4))
print(transformed_variable4)

# Uncommenting the code below will raise an error. Play around to see which other types are incompatible!!!
# bad_transformation = int(string_variable)
