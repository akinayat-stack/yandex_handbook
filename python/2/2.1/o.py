hour = int(input())
minutes = int(input())
t = int(input())
result = (hour * 60) + minutes + t
result_h = (result // 60) % 24
result_m = int(result % 60)
print(f"{result_h:02d}:{result_m:02d}")