import sys

# M : 주차장을 한 바퀴 도는 데 걸리는 시간 (분) (1 ≤ M ≤ 10^4)
M = int(sys.stdin.readline())

# K : 주차장의 온도 (켈빈) (250 ≤ K ≤ 320) - 문제에서 사용되지 않으나, 입력조건으로 입력하기기
K = int(sys.stdin.readline())

# C : 주차장을 돈 횟수 (1 ≤ C ≤ 10^4)
C = int(sys.stdin.readline())

# 총 소요 시간 = ( 한 바퀴 시간 × 돈 횟수 )
total_time = M * C

print(total_time)
