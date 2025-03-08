import sys

# T1, T2 : 입력되는 두 정수
T1, T2 = map(int, input().split())

if T1 <= T2 :
    print(T1)
else : 
    print(T2)