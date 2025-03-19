import sys

# S : 입력받는 문자열
while True:
    S = input()
    if S == "END":
        break
    print(S[::-1])