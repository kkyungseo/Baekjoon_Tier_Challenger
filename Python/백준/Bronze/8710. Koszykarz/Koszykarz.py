import sys

# 입력 받기
k, w, m = map(int, input().split())

if k >= w:
    print(0)
else:
    # 부족한 키 계산
    need = w - k
    
    # 나눗셈 올림으로 필요한 횟수 계산
    hits = (need + m - 1) // m
    
    print(hits)