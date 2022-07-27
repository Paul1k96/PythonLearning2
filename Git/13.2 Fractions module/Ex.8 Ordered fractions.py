from fractions import Fraction

n = int(input())

st = set()
for i in range(n):
    for j in range(n):
        if 0 < j/(i+1) < 1:
            st.add(Fraction(j, i+1))

print(*sorted(st), sep='\n')