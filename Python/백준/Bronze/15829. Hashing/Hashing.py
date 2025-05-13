import sys

L = int(input())
s = input()

# 문자열 해싱에서 r은 기수 (base) 역할 (일반적인 문자열 해싱에서의 기수 값)
r = 31
# 해시범위 제한, 모듈러 연산을 위한 값 (해시충돌가능성을 줄이고 수가 너무 커지지 않게 조절)
M = 1234567891
# 해시 값을 저장할 변수이며, 누적 합을 저장하는 용도
hash_value = 0

for i in range(L):
    # a부터 z까지를 1~26으로 변환
    char_value = ord(s[i]) - ord('a') + 1
    hash_value += char_value * (r ** i)
    # 매번 나눠주는 것으로 오버플로우 방지
    hash_value %= M  

print(hash_value)