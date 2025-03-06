import sys

# N : 사람의 수
# S : 주식의 개수
for line in sys.stdin:
    if line.strip():
        N, S = map(int, line.split())
        print(S // (N + 1))