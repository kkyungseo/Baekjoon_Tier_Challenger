import sys

jinho_mbti = input().strip()

# N : 친구 수 입력
N = int(input())

# same_count : 같은 MBTI 유형의 친구 수 카운트
same_count = 0

for _ in range(N):
    friend_mbti = input().strip()
    if friend_mbti == jinho_mbti:
        same_count += 1

# 출력
print(same_count)