def game(p1,p2):
    if p1 == p2:
        return 'ничья'
    if p1 == 'бумага' and p2 == 'камень' or p1 == 'камень' and p2 =='ножницы' or p1 == 'ножницы' and p2 == 'бумага':
        return 'Тимур'
    else:
        return 'Руслан'
print(game(input(),input()))
