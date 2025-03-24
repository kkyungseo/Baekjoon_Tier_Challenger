import sys

# N : 설문조사를 한 사람의 수
N = int(input())

cute_count = 0

for _ in range(N):
    opinion = int(input())
    cute_count += opinion  

if cute_count > N // 2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")