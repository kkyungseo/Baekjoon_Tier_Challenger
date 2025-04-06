import sys

# 입력
a, b = map(int, input().split())

# total : 총 조각의 수
total = a * b

# 공평한 분할을 위해 2로 나눈 몫을 측정
half1 = total // 2
half2 = total - half1

# 차이 계산 (문제의 요지는 두 구역의 조각의 개수의 차이, 음수 출력 방지를 위해 절댓값 이용)
difference = abs(half1 - half2)

# 가로로 자르기: x 행 vs (a - x) 행
row_diff = abs(a - 2 * (a // 2)) * b

# 세로로 자르기: y 열 vs (b - y) 열
# 차이: |b - 2y| * a
col_diff = abs(b - 2 * (b // 2)) * a

# 실제로 가능한 절단 방식 중 차이가 더 작은 것을 선택
difference = min(row_diff, col_diff)

print(difference)