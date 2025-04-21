import sys

N, M = map(int, input().split())

limit_speed = [0] * 100
run_speed = [0] * 100

# 제한속도의 입력
idx = 0
for _ in range(N):
    length, speed = map(int, input().split())
    for i in range(length):
        limit_speed[idx] = speed
        idx += 1

# 연정속도의 입력
idx = 0
for _ in range(M):
    length, speed = map(int, input().split())
    for i in range(length):
        run_speed[idx] = speed
        idx += 1

# 속도 초과 계산
max_over_speed = 0
for i in range(100):
    if run_speed[i] > limit_speed[i]:
        max_over_speed = max(max_over_speed, run_speed[i] - limit_speed[i])

print(max_over_speed)