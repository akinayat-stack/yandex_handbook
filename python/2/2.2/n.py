num = int(input())
one = num // 100
two = (num // 10) % 10
three = num % 10
nums = [one, two, three]
nums_sorted = sorted(nums)
if nums_sorted[0] == 0:
    min = nums_sorted[1] * 10 + nums_sorted[0]
else:
    min = nums_sorted[0] * 10 + nums_sorted[1]
max = nums_sorted[2] * 10 + nums_sorted[1]
print(min, max)