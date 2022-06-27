def chess_knight(sym):
    chess = [['.']*8 for _ in range(8)]
    x, y =ord(sym[0].upper())-65, int(sym[1])-1
    chess[y][x] = 'N'
    for r in range(8):
        for c in range(8):
            if (x - c)**2 + (y - r)**2 == 5:
                chess[r][c] = '*'
    return chess

play = chess_knight(input())
play.reverse()
for i in play:
    print(*i)