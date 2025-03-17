import sys
from collections import Counter

# S : 입력받는 문자열
S = input().strip()

# 입력받은 문자열에서 알파벳 개수 세기
count = Counter(S)

# 측정을 위한 알파벳 리스트 
alphabet_list = list("abcdefghijklmnopqrstuvwxyz")

# a부터 z까지 개수를 리스트로 저장 후 출력
# result에 *을 활용하여 요소간의 공백 처리
result = [count[c] for c in alphabet_list]
print(*result)