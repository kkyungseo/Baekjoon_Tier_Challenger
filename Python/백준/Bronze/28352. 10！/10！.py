import sys
import math

# N : 주어지는 정수
N = int(sys.stdin.readline())

# N! 계산 
factorial = math.factorial(N)

# 1주 = 604,800초
seconds_per_week = 7 * 24 * 60 * 60

# N!초를 주로 변환
weeks = factorial // seconds_per_week

print(weeks)
