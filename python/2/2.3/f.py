a = int(input())
b = int(input())
min = min(a, b)
while b != 0:
    a, b = b, a % b
print(a)
