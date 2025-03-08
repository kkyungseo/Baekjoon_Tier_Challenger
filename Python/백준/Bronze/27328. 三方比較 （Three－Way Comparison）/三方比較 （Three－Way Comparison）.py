import sys

# A, B : 입력받는 두 정수
A = int(input())
B = int(input())

if A < B:
    print(-1)
elif A == B:
    print(0)
else:
    print(1)