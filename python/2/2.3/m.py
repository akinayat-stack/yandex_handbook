n = int(input())
first = input()
for i in range(n - 1):
    name = input()
    if name < first:
        first = name
print(first)
