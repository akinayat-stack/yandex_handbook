num = int(input())
one = num // 1000
two = (num // 100) % 10
three = (num // 10) % 10
four = num % 10
if one == four and two == three:
    print("YES")
else:
    print("NO")