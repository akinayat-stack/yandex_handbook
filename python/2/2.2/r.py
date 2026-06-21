a = int(input())
b = int(input())
c = int(input())
max = max(a, b, c)
min = min(a, b, c)
mid = a + b + c - max - min
if max ** 2 == min ** 2 + mid ** 2:
    print("100%")
elif max ** 2 > min ** 2 + mid ** 2:
    print("велика")
else:
    print("мала")