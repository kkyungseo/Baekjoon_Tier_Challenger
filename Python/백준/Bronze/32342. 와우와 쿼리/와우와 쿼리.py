import sys

# Q : 소리의 개수 
Q = int(input())

# 문자열 입력에 따른 처리
for i in range(Q):
    # S : 입력받는 문자열
    S = input()

    # WOW의 개수 측정
    count = 0
    # WOW는 길이 3이므로 [j, j+3]에서 탐색
    for j in range(len(S) - 2):  
        if S[j:j+3] == "WOW":
            count += 1

    # 결과 출력
    print(count)