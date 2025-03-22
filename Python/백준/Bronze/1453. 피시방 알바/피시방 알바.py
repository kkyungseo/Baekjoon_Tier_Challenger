import sys
import math

# N : 손님의 수
N = int(input())

# seats : 손님이 앉고 싶어하는 자리들
seats = list(map(int, input().split()))

# occupied : 이미 앉은 자리들을 기록하는 set
occupied = set()  
# rejected : 거절된 사람 수
rejected = 0  

# 리스트에서 중복값이 발생한 수를 기록
for seat in seats:
    if seat in occupied:
        rejected += 1  
    else:
        occupied.add(seat)  

print(rejected)