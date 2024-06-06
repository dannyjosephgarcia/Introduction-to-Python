list_variable = [1, 2, 3]
for number in list_variable:
    print(number)

for number in list_variable:
    new_variable = number + 1
    print(new_variable)

size = len(list_variable)
for i in range(size):
    print(list_variable[i])

for i in range(size):
    print(i)

new_list_variable = [6, 7, 8, 9, 10]
size2 = len(new_list_variable)
for i in range(2, size2):
    print(size2)

dict_variable = {'key1': 1, 'key2': 2}
for key in dict_variable.keys():
    print(key)

for value in dict_variable.values():
    print(value)

for key, value in dict_variable.items():
    print(key)
    print(value)


list_comprehension = [number for number in range(1, 11)]
print(list_comprehension)

