from collections import deque

def solve():
    # N : 참가자 수
    N = int(input())
    # slices_needed : 각 참가자가 필요한 피자 조각 수
    slices_needed = list(map(int, input().split()))  
    
    # 대기열을 위한 deque
    queue = deque()  
    # result : 각 참가자가 완료된 시간을 저장할 리스트
    result = [0] * N  
    
    # 각 참가자 ~ (인덱스, 필요한 조각 수)
    for i in range(N):
        queue.append((i, slices_needed[i]))
    
    # current time :  현재 시간
    current_time = 0 
    while queue:
        index, slices = queue.popleft()    # 대기열에서 첫 번째 참가자 가져오기
        current_time += 1                  # 1초 경과
        slices -= 1                        # 한 조각을 받음
        
        # 참가자가 더 많은 피자가 필요하면 다시 대기열에 추가
        if slices > 0:
            queue.append((index, slices))
        else:
            result[index] = current_time  # 모든 피자를 받은 시간 기록
    
    print(" ".join(map(str, result)))

solve()
