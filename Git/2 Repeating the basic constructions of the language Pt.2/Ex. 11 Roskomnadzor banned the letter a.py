word = input() + ' запретил букву'
for i in range(32):
    a = chr(ord('а')+i)
    if a in word:
        print(word, a)
        word = word.replace(a, '')
        word = ' '.join(word.split())



