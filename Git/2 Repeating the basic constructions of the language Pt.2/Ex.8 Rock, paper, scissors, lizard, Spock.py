def game(p1,p2):
    result = ['ничья','Руслан','Тимур']
    c = ['камень','ножницы','бумага','ящерица','Спок']
    if p1 == p2:
        return result[0]
    if p1+p2 in [c[0]+c[1], c[0]+c[3], c[1]+c[2], c[1]+c[3], c[2]+c[0], c[2]+c[4], c[3]+c[2], c[3]+c[4], c[4]+c[0], c[4]+c[1]]:
        return result[2]
    else:
        return result[1]
print(game(input(),input()))