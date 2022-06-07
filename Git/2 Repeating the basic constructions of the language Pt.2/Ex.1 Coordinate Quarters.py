n = int(input())
q1, q2, q3, q4 = 0, 0 ,0 ,0
for i in range(n):
    inp = input().split()
    x, y = int(inp[0]), int(inp[1])
    if x!=0 and y!=0:
        if x>0 and y>0:
            q1+=1
        if x<0 and y>0:
            q2+=1
        if x<0 and y<0:
            q3+=1
        if x>0 and y<0:
            q4+=1

print(f"Первая четверть: {q1}", f"Вторая четверть: {q2}", f"Третья четверть: {q3}", f"Четвертая четверть: {q4}", sep='\n')


