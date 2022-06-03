num = input()
num = num[-6::-1]+num[:-6:-1]
print(int(num))