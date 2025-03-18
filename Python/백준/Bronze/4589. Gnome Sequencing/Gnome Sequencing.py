import sys

# N : 입력되는 줄의 개수
N = int(input())


print("Gnomes:")

for _ in range(N):
    A, B, C = map(int, input().split())
    
    if (A <= B <= C) or (A >= B >= C):
        print("Ordered")
    else:
        print("Unordered")