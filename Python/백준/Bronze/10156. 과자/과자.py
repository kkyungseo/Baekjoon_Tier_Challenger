import sys

# K : 과자 한 개의 가격
# N : 사려고 하는 과자의 개수
# M : 현재 가지고 있는 돈의 개수
K, N, M = map(int, input().split())

if K * N >= M :
    print(K * N - M)
else : 
    print("0")