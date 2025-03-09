import sys

# N : 대학 ~ 지하철 걷는 시간
# A : 정류소 ~ 집으로 가는 버스
# B : 역 ~ 집으로 가는 열차
N, A, B = map(int, input().split())
if A < B:
    print("Bus")
elif A > B:
    print("Subway")
else:
    print("Anything")