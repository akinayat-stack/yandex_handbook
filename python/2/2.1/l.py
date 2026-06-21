num_1 = int(input())
num_2 = int(input())
one_1 = int(num_1 / 100)
one_2 = int(num_2 / 100)
two_1 = int((num_1 / 10) % 10)
two_2 = int((num_2 / 10) % 10)
three_1 = num_1 % 10
three_2 = num_2 % 10
result_1 = (one_1 + one_2) % 10 * 100
result_2 = (two_1 + two_2) % 10 * 10
result_3 = (three_1 + three_2) % 10
print(result_1 + result_2 + result_3)