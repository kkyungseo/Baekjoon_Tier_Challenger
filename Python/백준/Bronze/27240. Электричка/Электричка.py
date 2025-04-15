import sys

# n, a, b : 입력받는 세 개의 정수
n, a, b = map(int, input().split())

# s, t : 출발역과 도착역
s, t = map(int, input().split())

# 도시 구간: a+1 ~ b-1
city_start = a + 1
city_end = b - 1

if city_start <= s <= city_end and city_start <= t <= city_end:
    print("City")
elif (s <= a and t <= a) or (s >= b and t >= b):
    print("Outside")

else:
    print("Full")