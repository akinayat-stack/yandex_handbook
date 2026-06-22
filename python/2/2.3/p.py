n = int(input())
num = n
m = 0

while n != 0:
    d = n % 10
    m = m * 10 + d
    n = n // 10

if m == num:
    print("YES")
else:
    print("NO")