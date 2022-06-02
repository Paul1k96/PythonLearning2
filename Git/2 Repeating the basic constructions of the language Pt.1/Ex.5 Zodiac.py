you_age = int(input())
zodiac = ["Дракон","Змея","Лошадь","Овца","Обезьяна","Петух","Собака","Свинья","Крыса","Бык","Тигр","Заяц"]
ages = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011]
while you_age not in ages:
    if you_age<=1999:
        you_age+=12
    elif you_age>=2012:
        you_age-=12
for i in range(len(ages)):
     if you_age == ages[i]:
         print(zodiac[i])
