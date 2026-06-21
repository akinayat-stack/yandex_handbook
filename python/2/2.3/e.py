price = 0
while(p := float(input())) != 0:
    if p >= 500:
        price += p - (p * 0.1)
    else:
        price += p
print(price)
