import sys

# 입력 받기
E, S, M = map(int, input().split())

# 초기 연도
year = 1

# E, S, M은 각각의 수를 기준으로 순환
e, s, m = 1, 1, 1

# 조건 만족할 때까지 반복
while True:
    if e == E and s == S and m == M:
        print(year)
        break
            
    # 1씩 증가, 범위를 넘기면 다시 1로 작성
    e = e + 1 if e < 15 else 1
    s = s + 1 if s < 28 else 1
    m = m + 1 if m < 19 else 1
    year += 1