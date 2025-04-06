import sys

# Z : 테스트 케이스 수
Z = int(input())

for _ in range(Z):
    # 행(W), 열(K)
    W, K = map(int, input().split())
    
    total_cells = W * K
    
    max_tourists = total_cells // 2
    
    print(max_tourists)