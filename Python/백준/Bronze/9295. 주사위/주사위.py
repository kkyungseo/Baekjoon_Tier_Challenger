import sys

# T : 테스트 케이스의 개수
T = int(input())

for i in range(1, T+1) :
    N, M = map(int, input().split())
    result = N + M
    print(f"Case {i}: {result}")