import sys

# N, M : 행렬의 크기 (2차 행렬)
N,M = map(int, input().split())
# A, B : 두 가지 행렬
A,B = [],[]

# 조건에 따라 행렬을 구성
for i in range(N):
    a = list(map(int,input().split()))
    A.append(a)
        
for i in range(N):
    b = list(map(int,input().split()))
    B.append(b)

# 2차 행렬의 요소들을 같은 위치의 같은 요소들을 더해 결과를 구함
for i in range(N):
    for j in range(M):
        result = A[i][j] + B[i][j]
        print(result,end=' ')
    print()