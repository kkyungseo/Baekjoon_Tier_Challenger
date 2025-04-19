import sys

# N : 각 종류 치킨 마릿수
N = int(input())

# A, B, C : 각 종류의 치킨을 원하는 사람의 수
A, B, C = map(int, input().split())

result = min(N, A) + min(N, B) + min(N, C)

print(result)