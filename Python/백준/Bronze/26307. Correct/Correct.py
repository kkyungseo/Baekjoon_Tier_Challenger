import sys

# H, M : 문제풀이 시간
H, M = map(int, input().split())

result = (H - 9) * 60 + M

print(result)