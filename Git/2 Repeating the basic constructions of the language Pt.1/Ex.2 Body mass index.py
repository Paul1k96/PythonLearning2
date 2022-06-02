a, b = float(input()), float(input())
BMI = a/(b*b)
if 18.5<=BMI<=25:
    print("Оптимальная масса")
elif BMI<18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")
