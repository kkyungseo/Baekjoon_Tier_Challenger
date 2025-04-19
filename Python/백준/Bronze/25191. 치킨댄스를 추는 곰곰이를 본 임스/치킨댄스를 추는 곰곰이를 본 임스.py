import sys

# N : 치킨집에 있는 치킨의 총 개수
# A : 콜라의 개수 / B : 맥주의 개수
N = int(input())
A, B = map(int, input().split())

can = int((A // 2) + B)

print(min(N, can))