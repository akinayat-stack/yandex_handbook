n = int(input())
prev_h = 0
for i in range(n):
    b = int(input())
    h = b % 256
    r = (b // 256) % 256
    m = b // (256 * 256)
    calc_h = (37 * (m + r + prev_h)) % 256
    if h >= 100 or h != calc_h:
        print(i)
        break
    prev_h = h
else:
    print(-1)