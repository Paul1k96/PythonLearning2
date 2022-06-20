def chunk(txt, n):
    from math import ceil
    txt, count = ''.join(txt.split()), 0
    lst = []
    d = ceil(len(txt)/n)
    for i in range(d):
        lst+=[[]]
        for j in range(n):
            if count == len(txt):
                break
            lst[i] += [txt[count]]
            count+=1
    return lst

print(chunk(input(),int(input())))