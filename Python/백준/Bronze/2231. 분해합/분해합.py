import sys

# 전체 탐색을 위해 브루트포스 이용
def find_constructor(N):
    for i in range(max(1, N - 9 * len(str(N))), N):
        if i + sum(map(int, str(i))) == N:
            return i
    return 0

# 입력
N = int(input())

# 출력
print(find_constructor(N))