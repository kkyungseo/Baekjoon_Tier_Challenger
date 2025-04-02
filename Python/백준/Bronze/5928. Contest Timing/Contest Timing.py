import sys

D, H, M = map(int, input().split())

# 시작 시간 : 분 단위 변환
start = (11 * 24 * 60) + (11 * 60) + 11

# 종료 시간 : 분 단위 변환
end = (D * 24 * 60) + (H * 60) + M

# 대회 종료 시간이 시작 시간보다 빠르면 -1 출력
if end < start:
    print(-1)
else:
    print(end - start)