import sys

# 입력 받는 정보
a_x, a_y, a_z = map(int, input().split())
c_x, c_y, c_z = map(int, input().split())

# 계산법 정리
b_x = c_x - a_z
b_y = c_y // a_y
b_z = c_z - a_x

print(b_x, b_y, b_z)