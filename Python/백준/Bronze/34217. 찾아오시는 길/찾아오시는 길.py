import sys
input = sys.stdin.readline

# A : 출발지에서 한양대역까지 걸리는 시간 / B : 출발지에서 용답역까지 걸리는 시간
A, B = map(int, input().split())

# C : 한양대역에서 ITBT관까지 걸리는 시간 / D : 용답역에서 ITBT관까지 걸리는 시간
C, D = map(int, input().split())

# 한양대역 경로와 용답역 경로의 총 시간 계산
hanyang_time = A + C
yongdap_time = B + D

# 더 빠른 경로에 따라 출력
if hanyang_time < yongdap_time:
    print("Hanyang Univ.")
elif yongdap_time < hanyang_time:
    print("Yongdap")
else:
    print("Either")
