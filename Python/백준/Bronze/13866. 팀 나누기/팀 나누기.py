import math

# 입력
A, B, C, D = map(int, input().split())
skills = [A, B, C, D]

# 가능한 팀 조합
pairs = [
    ([A, B], [C, D]),
    ([A, C], [B, D]),
    ([A, D], [B, C])
]

# 가장 작은 스킬 차이 찾기
min_diff = math.inf

for team1, team2 in pairs:
    diff = abs(sum(team1) - sum(team2))
    min_diff = min(min_diff, diff)

print(min_diff)