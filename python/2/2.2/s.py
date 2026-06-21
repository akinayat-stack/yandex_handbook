x = float(input())
y = float(input())
if x ** 2 + y ** 2 > 100:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
else:
    cond_1 = x ** 2 + y ** 2 <= 100
    cond_2 = y <= 5
    cond_3 = 3 * y <= 5 * x + 35
    cond_4 = 4 * y >= (x + 1) ** 2 - 36
    cond_5 = x ** 2 + y ** 2 <= 25
    if (cond_1 and cond_2 and cond_3 and cond_4 and cond_5):
        print("Опасность! Покиньте зону как можно скорее!")
    elif x ** 2 + y ** 2 <= 100:
        print("Зона безопасна. Продолжайте работу.")