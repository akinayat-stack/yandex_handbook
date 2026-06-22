low = 1
high = 1000
while True:
    guess = (low + high) // 2
    print(guess, flush=True)
    answer = input()
    if answer == "Угадал!":
        break
    elif answer == "Меньше":
        high = guess - 1
    elif answer == "Больше":
        low = guess + 1