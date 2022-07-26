from random import shuffle
names = []
for _ in range(int(input())):
    names += [input()]

names_len = len(names)
names_copy = names.copy()
count = 0
while count != names_len:
    shuffle(names_copy)
    for i in range(names_len):
        if names[i] == names_copy[i]:
            count = 0
            break
        else:
            count += 1

names_dict = dict(tuple([(names[i], names_copy[i]) for i in range(names_len)]))

for key, value in names_dict.items():
    print(key, '-', value)