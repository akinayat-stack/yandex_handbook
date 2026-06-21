amount = 0
while(str := input()) != "Приехали!":
    if "зайка" in str:
        amount += 1
print(amount)
