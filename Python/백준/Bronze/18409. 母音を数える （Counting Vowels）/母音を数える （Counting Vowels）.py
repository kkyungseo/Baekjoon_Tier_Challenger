import sys

N = int(input())  
S = input()      

vowels = 'aiueo'

count = 0

# 문자열 S에서 각 문자 확인
for char in S:
    if char in vowels:  
        count += 1

print(count)