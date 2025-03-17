import sys
from collections import Counter

# N : 입력받는 기준이 되는 정수
N = int(input())

# num : 입력받은 수를 리스트로 저장
num = list(map(int, input().split()))

# N과 일치하는 요소의 개수 카운팅
print(num.count(N))