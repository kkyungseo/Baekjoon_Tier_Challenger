import sys

# S : 입력받는 문자열 
S = input()       

# 모음 집합
vowels = 'aiueo'

# 모음의 개수를 세기 위한 변수
count = 0

for char in S:
    if char in vowels:  
        count += 1

print(count)