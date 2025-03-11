import sys

# N : 숫자의 개수
N = int(input()) 
moves = list(map(int, input().split())) 

total_movement = sum(moves)

if total_movement > 0:
    print("Right")
elif total_movement < 0:
    print("Left")
else:
    print("Stay")