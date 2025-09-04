import sys

# n : 사람의 수
n = int(input())

# p : 각 사람이 돈을 인출하는데 걸리는 시간
p = list(map(int, input().split()))

# 처리 시간을 오름차순으로 정렬
p.sort()

# total_time : 각 사람이 돈을 인출하는데 필요한 시간의 합
total_time = 0

# 각 사람의 대기 시간 계산 (for문 사용)
for i in range(n):
    # i번째 사람의 대기 시간 == 앞의 모든 사람들의 처리 시간 합
    waiting_time = sum(p[:i+1])
    total_time += waiting_time

# 최소값 출력
print(total_time)
