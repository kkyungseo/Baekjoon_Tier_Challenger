import sys

# t : 테스트케이스의 개수
t = int(input())

# 가위바위보 승패 판별 딕셔너리 (이기는 경우만 저장)
win_cases = {'R': 'S', 'P': 'R', 'S': 'P'}

for _ in range(t):
    n = int(input())
    score1, score2 = 0, 0

    for _ in range(n):
        p1, p2 = input().split()
        if p1 != p2:  # 비기지 않은 경우만 판단
            if win_cases[p1] == p2:
                score1 += 1
            else:
                score2 += 1

    # 최종 승자 출력
    print("Player 1" if score1 > score2 else "Player 2" if score1 < score2 else "TIE")