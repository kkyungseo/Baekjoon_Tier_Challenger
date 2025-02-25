import sys

def solve(N):
    if N % 9 == 0 or N % 3 == 2:
        print("TAK")
    else:
        print("NIE")

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    solve(N)