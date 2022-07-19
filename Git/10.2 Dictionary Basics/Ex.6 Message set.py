sym_dict = {'1': ('.', ',', '?', '!', ':'),
            '2': ('A', 'B', 'C'),
            '3': ('D', 'E', 'F'),
            '4': ('G', 'H', 'I'),
            '5': ('J', 'K', 'L'),
            '6': ('M', 'N', 'O'),
            '7': ('P', 'Q', 'R', 'S'),
            '8': ('T', 'U', 'V'),
            '9': ('W', 'X', 'Y', 'Z'),
            '0': ' '}

txt = tuple(input().upper())
for i in txt:
    for key in sym_dict:
        if i in sym_dict[key]:
            print(key*(sym_dict[key].index(i)+1), end='')


