import sys
import math

# T : 입력받는 테스트 케이스 개수
T = int(sys.stdin.readline().strip())  

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split()) 
    # result : 조합의 계산 결과
    result = math.comb(M, N) 
    print(result)