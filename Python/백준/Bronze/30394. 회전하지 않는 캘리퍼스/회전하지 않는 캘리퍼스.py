import sys

# N : 점의 개수
N = int(sys.stdin.readline().strip())

# y 좌표 최솟값, 최댓값 초기화
min_y, max_y = float('inf'), float('-inf')

# 점의 좌표 입력 받기
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    min_y = min(min_y, y)
    max_y = max(max_y, y)

# 캘리퍼스로 측정한 거리값 출력
print(max_y - min_y)