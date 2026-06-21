num = int(input())
one = num // 100
two = (num // 10) % 10
three = num % 10
first = (one + two)
second = (two + three)
if first < second:
    print(second * 10 + first)
else:
    print(first * 10 + second)