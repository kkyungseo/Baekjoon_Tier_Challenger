import sys
from collections import deque

# n : 컴퓨터의 수
n = int(input())
# m : 네트워크 연결 쌍의 수
m = int(input())

# 그래프를 인접 리스트로 표현
graph = [[] for _ in range(n + 1)]

# 네트워크 연결 정보 입력
# a, b : 네트워크 연결 매칭 번호 정보 
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS(너비우선탐색)로 1번 컴퓨터에서 시작해서 연결된 모든 컴퓨터 찾기
visited = [False] * (n + 1)
queue = deque([1])
visited[1] = True
count = 0

while queue:
    current = queue.popleft()
    
    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)
            count += 1

print(count)
