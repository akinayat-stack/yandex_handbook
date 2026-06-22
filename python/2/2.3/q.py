n = int(input())
ans = 0
p = 1

while n != 0:
    if n % 10 % 2 != 0:
        ans += (n % 10) * p
        p *= 10
    n = n // 10

print(ans)