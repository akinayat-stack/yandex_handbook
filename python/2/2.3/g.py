a = int(input())
b = int(input())
sum = a * b
min = min(a, b)
while b != 0:
    a, b = b, a % b
print(int(sum / a))

