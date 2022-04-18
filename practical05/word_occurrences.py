numbers = {}
content = input("Text: ")
words = content.split()
for word in words:
    frequency = numbers.get(word, 'none')
    numbers[word] = frequency + 1
words = list(numbers.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, numbers[word]))