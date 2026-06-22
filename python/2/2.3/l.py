n = int(input())
result = 0
while n != 0:
    last = n % 10
    if last > result:
        result = last
    n //= 10
print(result)