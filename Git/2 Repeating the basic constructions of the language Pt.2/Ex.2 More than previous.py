count, numb = 0, input().split()
for i in range(1, len(numb)):
    if int(numb[i-1])<int(numb[i]):
        count+=1
print(count)