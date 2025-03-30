import sys

def find_min_time_to_buy_bread(N, stores):
    # 초기값을 -1로 설정하여, 빵을 살 수 없는 경우를 바로 처리
    min_time = -1  
    
    # 각 가게에 대해 처리
    for i in range(N):
        # A : 걸리는 시간
        # B : 빵이 도착할 시간
        A, B = stores[i]  
        
        # 빵을 살 수 있다면
        if A <= B: 
             # 처음 또는 더 작은 시간이 나오면 갱신
            if min_time == -1 or A < min_time: 
                min_time = A
    
    return min_time

# N : 가게의 수
N = int(input())  
# 각 가게의 (A, B) 정보
stores = [tuple(map(int, input().split())) for _ in range(N)]  

print(find_min_time_to_buy_bread(N, stores))