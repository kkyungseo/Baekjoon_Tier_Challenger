import sys

# A, B : 입력받는 두 수
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    if A > B:
        print("Yes")
    else:
        print("No")