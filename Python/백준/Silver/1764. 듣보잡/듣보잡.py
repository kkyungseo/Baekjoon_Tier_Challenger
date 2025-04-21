import sys
input = sys.stdin.readline

# 이름의 개수
n, m = map(int, input().split())

listen = set()
for _ in range(n):
    listen.add(input().strip())

see = set()
for _ in range(m):
    see.add(input().strip())

# 교집합을 구하고 사전순으로 이름을 출력
result = sorted(listen & see)

# 출력
print(len(result))
for name in result:
    print(name)