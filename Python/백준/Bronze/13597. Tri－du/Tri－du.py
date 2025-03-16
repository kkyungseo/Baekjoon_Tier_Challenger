import sys

# A, B : 입려받는 두 개의 숫자
A, B = map(int, input().split())
# 세 번째 숫자 입력 전에 더 가능성이 높은 수는 둘 중 큰 숫자
print(max(A, B))