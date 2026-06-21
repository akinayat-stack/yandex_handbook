num = int(input())

one = num // 100
two = (num // 10) % 10
three = num % 10

mx = max(one, two, three)
mn = min(one, two, three)
mid = one + two + three - mx - mn

if mn + mx == mid * 2:
    print("YES")
else:
    print("NO")