def dictionary(word_list):
    word_dict = {}
    for word in word_list:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict


word1 = [i for i in list(input().lower()) if i not in '.,?!:;() ']
word2 = [i for i in list(input().lower()) if i not in '.,?!:;() ']
dict1, dict2 = dictionary(word1), dictionary(word2)

print(['NO', 'YES'][dict1 == dict2])
