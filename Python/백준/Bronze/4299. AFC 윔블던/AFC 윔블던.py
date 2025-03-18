import sys

# A : 두 팀 점수의 합
# B : 두 팀 점수의 차 
A, B = map(int, input().split())

if (A + B) % 2 or (A - B) % 2 or A < B:
    print(-1)
else:
    print((A + B) // 2, (A - B) // 2)