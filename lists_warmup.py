numbers = [3, 1, 4, 1, 5, 9, 2]
'''
print(numbers[0])---3
print(numbers[-1])---2
print(numbers[3])---1
print(numbers[:-1])---[3, 1, 4, 1, 5, 9]
print(numbers[3:4])---[1]
5 in numbers---True
7 in numbers---False
"3" in numbers---print(0)
numbers + [6, 5, 3]---[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
'''
numbers[0] = "ten"
print(numbers)

numbers[0] = 1
print(numbers)

print(numbers[2:6])

print(5 in numbers)
