import sys
input = sys.stdin.readline

# 재귀 깊이 제한 증가 (깊은 재귀 호출로 인한 스택 오버플로우 방지)
sys.setrecursionlimit(100000)  

# V : 정점의 개수 (1번부터 V까지 정점의 번호가 매겨져 있음)
# E : 간선의 개수
V, E = map(int, input().split()) 

# 간선 정보 저장
edges = []  # (가중치, 정점1, 정점2)

# A, B, C : 간선에 대한 정보
# A번 정점과 B번 정점이 가중치 C인 간선으로 연결
for _ in range(E):
    A, B, C = map(int, input().split()) 
    edges.append((C, A, B))

# 초기화
# 부모 테이블과 랭크 테이블
parent = [i for i in range(V+1)]
rank = [0] * (V+1)

# find 함수 : 노드의 루트 찾기 (경로 압축)
def find(x):
    if parent[x] != x:  # 루트가 아니면 재귀 호출
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

# union 함수 : 두 집합을 합치기 (랭크 기반 최적화)
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    
    if root_x == root_y:
        return False  # 이미 같은 집합
    
    # 랭크가 낮은 트리를 높은 트리 아래에 붙이기
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1
    
    return True  

# 간선을 가중치 기준으로 오름차순 정렬
edges.sort()

# 크루스칼 알고리즘
# 최소 스패닝 트리의 가중치
min_cost = 0  
edge_count = 0

for cost, u, v in edges:
    # 사이클이 생기지 않을 때만 추가
    if union(u, v):
        min_cost += cost
        edge_count += 1
        
        # MST는 (정점 수 - 1)개의 간선을 가짐
        if edge_count == V - 1:
            break

# 출력 (최소 스패닝 트리의 가중치 출력)
print(min_cost)
