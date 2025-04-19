import sys

# N : 가게의 개수
N = int(sys.stdin.readline())

# d : KOI 빵을 살 수 있는 가장 이른 시각 (b 기준)
d = 10**9  

for _ in range(N):
    # A : 현재 위치에서 가게까지 가는 데 걸리는 시간
    # B : 현재 시점에서 빵이 들어올 때까지의 시간
    A, B = map(int, sys.stdin.readline().split())
    
    if A <= B and B < d:
        d = B

# 아무 조건에도 만족하지 않으면 d는 그대로 1e9일 것이므로 -1 출력
print(-1 if d == 10**9 else d)