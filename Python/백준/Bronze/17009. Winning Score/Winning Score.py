import sys

# 사과 팀
apple_3 = int(input())
apple_2 = int(input())
apple_1 = int(input())
apple_score = apple_3 * 3 + apple_2 * 2 + apple_1 * 1

# 바나나 팀 
banana_3 = int(input())
banana_2 = int(input())
banana_1 = int(input())
banana_score = banana_3 * 3 + banana_2 * 2 + banana_1 * 1

if apple_score > banana_score:
    print('A')
elif banana_score > apple_score:
    print('B')
else:
    print('T')