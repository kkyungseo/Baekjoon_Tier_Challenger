import sys

# w : 직사각형의 가로 길이 입력력 (1 ≤ w ≤ 10^4)
w = int(sys.stdin.readline())

# l : 직사각형의 세로 길이 입력 (1 ≤ l ≤ 10^4)
l = int(sys.stdin.readline())

# 총 학생 수 = ( 가로 × 세로 )
total_students = w * l

print(total_students)
