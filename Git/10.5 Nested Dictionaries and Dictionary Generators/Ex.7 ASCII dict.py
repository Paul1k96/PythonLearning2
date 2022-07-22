# the key is a string - an element of the words list, and the value - a list of the corresponding ASCII codes of characters of the given string.

words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {i: [ord(j) for j in i] for i in words}
print(result)
