mrx = [input().split() for _ in range(int(input()))]
print(sum([int(mrx[i][i]) for i in range(len(mrx[0]))]))