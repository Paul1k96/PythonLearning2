mtx = [ list(map(int, input().split())) for _ in range(int(input()))]
for r in range(len(mtx)):
    a = len(mtx[r])
    count = 0
    for c in range(a):
        avg = sum(mtx[r])/a
        if mtx[r][c]> avg:
            count+=1
    print(count)
