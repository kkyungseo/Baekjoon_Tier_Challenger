import sys

# N : 기록를 하는 날짜 기간 
N = int(input())
# train_days : 운동 여부 리스트 (0과 1로 구분)
train_days = list(map(int, input().split()))  

# muscle : 총 근육 증가량 (초기값 설정)
muscle = 0 

for i in range(N):
    x, y = map(int, input().split())  
    # x : 아침 체중
    # y : 저녁체중
    if train_days[i] == 1 and y > x:  
        muscle += (y - x)  
        
print(muscle)