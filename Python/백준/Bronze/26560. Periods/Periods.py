import sys

n = int(input())
    
for _ in range(n):
    sentence = input()
    # strip()을 써서 공백 제거 후 끝이 '.'인지 확인
    if not sentence.strip().endswith('.'):
        sentence += '.'
    print(sentence)