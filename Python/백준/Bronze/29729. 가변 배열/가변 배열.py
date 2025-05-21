import sys
input = sys.stdin.readline

S, N, M = map(int, input().split())

# cnt : 실제 저장된 데이터 수
cnt = 0   

for i in range(N + M):
    num = int(input())
    
    if num == 1:
        if S == cnt:
            S += S  # 배열 용량이 꽉 찼으면 2배로 증가
        cnt += 1  # 데이터 추가
    else:
        cnt -= 1  # 데이터 삭제

print(S)