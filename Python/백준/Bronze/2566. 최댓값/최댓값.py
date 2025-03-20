import sys

input = sys.stdin.readline

# ans : for 문 동안 발견되는 최댓값 저장
# -1 로 설정하여 0 이상의 숫자들과 비교될 수 있도록 설정
ans = -1

for i in range(9):
    row = list(map(int, input().split()))
    max_num = max(row)
    if ans < max_num:
        ans = max_num
        # x : 행의 번호
        # y : 열의 번호
        x = i + 1
        y = row.index(max_num) + 1

print(ans)

print(x, y)