n = int(input())
d = 2
nums = []
while n > 1:
    if n % d == 0:
        nums.append(d)
        n //= d
    else:
        d += 1
print(" * ".join(map(str, nums)))