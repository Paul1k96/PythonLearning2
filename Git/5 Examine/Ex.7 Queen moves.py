def chess_queen(sym):
    chess = [['.']*8 for _ in range(8)]
    x, y =ord(sym[0].upper())-65, int(sym[1])-1

    for r in range(8):
        for c in range(8):
            if r-y == c-x or r + c == x+y or c == x or r == y:
                chess[r][c] = '*'
    chess[y][x] = 'Q'

    return chess

play = chess_queen(input())
play.reverse()
for i in play:
    print(*i)