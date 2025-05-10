# 입력
N = int(input())
finished = list(map(int, input().split()))

# 1부터 N까지의 총합에서 완주한 선수들의 번호를 뺌
total = N * (N + 1) // 2
missing = total - sum(finished)

print(missing)