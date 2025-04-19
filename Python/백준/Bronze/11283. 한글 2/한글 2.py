import sys

# char : 입력받는 한 글자
char = input().strip()  

# 유니코드 기반의 글자 순서 출력
print(ord(char) - ord('가') + 1)
