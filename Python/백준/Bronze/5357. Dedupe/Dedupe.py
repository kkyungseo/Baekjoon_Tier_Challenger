import sys

# N : 입력받는 테스트 케이스 개수
N = int(input())  

for _ in range(N):
    s = input().strip()
    print(''.join(s[i] for i in range(len(s)) if i == 0 or s[i] != s[i - 1]))