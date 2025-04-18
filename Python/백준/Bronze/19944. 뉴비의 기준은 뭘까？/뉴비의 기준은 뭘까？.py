import sys

# N, M : 입력받는 세 정수
N, M = map(int, input().split())

if M == 2 or M == 1 :
    print("NEWBIE!")
elif M > 2 and M <= N :
    print("OLDBIE!")
else :
    print("TLE!")