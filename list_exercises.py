# 1.
# numbers = []
# user_add_numbers = int(input("Please input 5 numbers"))
# numbers.append(user_add_numbers)
# print("The first number is {}".format(numbers[0]))
# print("The last number is {}".format(numbers[4]))
# print("The smallest number is {}".format(min(numbers)))
# print("The largest number is {}".format(max(numbers)))
# print("The average of the numbers is".format(sum(numbers)/len(numbers)))

# 2.
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Please input your name")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")