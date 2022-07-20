def dictionary(word_list):
    word_dict = {}
    for word in word_list:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict


dict1, dict2 = dictionary(list(input())), dictionary(list(input()))

print(['NO', 'YES'][dict1 == dict2])
