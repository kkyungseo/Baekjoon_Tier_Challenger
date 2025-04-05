import sys

# 입력 받기 (1 <= N <= 11172)
N = int(input())  

# 한글 '가'의 유니코드 시작점은 44032
start_code = 44032

# N번째 글자는 '가'부터 시작하여 N-1 만큼 떨어진 문자
letter = chr(start_code + N - 1)

print(letter)