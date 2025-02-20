# N : 줄에 대한 조건 
N = int(input())

# 별의 개수가 증가하는 섹션 
for i in range(1, N + 1):
    print(" " * (N - i) + "*" * (2 * i - 1))
    
# 별의 개수가 감소하는 섹션 (역순출력)
for i in range(N - 1, 0 , -1) : 
    print(" " * (N - i) + "*" * (2 * i -1))