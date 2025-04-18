import sys

# N, M : S 모양의 블록, A 모양의 블록
N, M = map(int, input().split())

# 하나의 블럭을 만들기 위해 필요한 블록의 개수 : S 모양 2개, A 모양 2개 
result = min(N, M) // 2

print(result)