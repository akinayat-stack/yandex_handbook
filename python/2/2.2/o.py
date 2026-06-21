num_1 = int(input())
a = num_1 // 10
b = num_1 % 10
num_2 = int(input())
c = num_2 // 10
d = num_2 % 10
nums = [a, b, c, d] 
nums_sorted = sorted(nums)
max = nums_sorted[3]
min = nums_sorted[0]
rest = (a + b + c + d - max - min) % 10
print(max * 100 + rest * 10 + min)