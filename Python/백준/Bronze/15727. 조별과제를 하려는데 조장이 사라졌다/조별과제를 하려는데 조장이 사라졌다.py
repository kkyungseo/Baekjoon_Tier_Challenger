import sys

# L : 성우의 현재 위치 ~ 민건이의 집의 거리
L = int(input())

if L % 5 == 0 :
    print(L // 5)
else :
    print(L // 5+1)