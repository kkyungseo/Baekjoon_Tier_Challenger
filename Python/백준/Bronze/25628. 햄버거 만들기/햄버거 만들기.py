import sys

# A : 햄버거 빵의 개수
# B : 햄버거 패티의 개수
A, B = map(int, input().split())

print(min(A // 2, B))