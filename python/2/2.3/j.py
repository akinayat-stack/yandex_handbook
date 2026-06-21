x = 0
y = 0
while (str := input()) != "СТОП":
    n = int(input())
    if str == "СЕВЕР":
        y += n
    elif str == "ЮГ":
        y -= n
    elif str == "ЗАПАД":
        x -= n
    elif str == "ВОСТОК":
        x += n
print(x)
print(y)