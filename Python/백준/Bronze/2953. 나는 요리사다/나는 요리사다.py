import sys

max_score = 0
winner = 0

# 참가자는 1번부터 5번까지 고정
for i in range(1, 6):  
    scores = list(map(int, sys.stdin.readline().split()))
    total = sum(scores) 
    
    # 최고 점수 갱신
    if total > max_score:  
        max_score = total
        winner = i

print(winner, max_score)