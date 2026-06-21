start = int(input())
end = int(input())
if start > end:
    s = -1
for i in range(start, end + s, s):
    print(i, end = " ")