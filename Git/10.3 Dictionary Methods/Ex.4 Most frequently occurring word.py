s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana ' \
    'banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes ' \
    'melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit ' \
    'barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit ' \
    'strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot ' \
    'barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley ' \
    'lime grapefruit pomegranate barley'

result = {}
word_list = [i for i in s.split()]
for word in word_list:
    result[word] = result.get(word, 0) + 1

mx_dig = max(result[key] for key in result)
result_copy = result.copy()
for key,value in result_copy.items():
    if value != mx_dig:
        del result[key]
print(min(result))