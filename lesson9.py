import collections

integer_variable = 1
float_variable = 13.2
string_variable = "Hello World"
boolean_variable_true = True
boolean_variable_false = False
none_variable = None

# Mutable: Any 'object' that can be altered
# Immutable: Any 'object' that cannot be altered
# Time complexity: The amount of RELATIVE time it takes for an operation to execute

# FIFO: First In, First Out
# LIFO: Last In, First Out

queue_variable = collections.deque()
queue_variable.append(2)
queue_variable.append(3)
queue_variable.append(4)
print(queue_variable[0])

print(queue_variable)

# Mess around with these operations (uncomment)
# queue_variable.pop()
# queue_variable.popleft()

first_element = queue_variable.popleft()
last_element = queue_variable.pop()
