result = {}
word_list = [i.strip('.,?!:;()').lower() for i in input().split()]

for word in word_list:
    result[word] = result.get(word, 0) + 1

min_dig = min(result[key] for key in result)
result_copy = result.copy()
for key,value in result_copy.items():
    if value != min_dig:
        del result[key]
print(min(result))