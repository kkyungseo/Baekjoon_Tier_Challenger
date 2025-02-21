N = int(input())
box = 1
cnt = 1

while N > box:
    box += 6 * cnt
    cnt += 1
print(cnt)