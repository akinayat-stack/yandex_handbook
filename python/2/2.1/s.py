name = input()
price = int(input())
weight = int(input())
money = int(input())

total = price * weight
change = money - total

print("=" * 16 + "Чек" + "=" * 16)

print("Товар:" + name.rjust(35 - len("Товар:")))

line = f"{weight}кг * {price}руб/кг"
print("Цена:" + line.rjust(35 - len("Цена:")))

print("Итого:" + f"{total}руб".rjust(35 - len("Итого:")))

print("Внесено:" + f"{money}руб".rjust(35 - len("Внесено:")))

print("Сдача:" + f"{change}руб".rjust(35 - len("Сдача:")))

print("=" * 35)