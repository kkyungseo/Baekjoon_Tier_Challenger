# N : 정점의 개수
N = int(input())  
    
# 최소 거리 합을 가지는 트리는 선형 트리
print((N - 1) ** 2)
    
# 간선 출력 (선형 트리)
for i in range(2, N+1) :
    print(1, i)
        