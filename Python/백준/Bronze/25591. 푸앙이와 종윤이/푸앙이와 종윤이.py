import sys

# 입력
num1, num2 = map(int, input().split())

# a, b 계산
a = 100 - num1
b = 100 - num2

# c, d 계산
c = 100 - (a + b)
d = a * b

# q, r 계산
q = d // 100
r = d % 100

# 계산
front = c + q
back = r

# 출력
print(a, b, c, d, q, r)

# 십의 자리가 0이면 일의 자리만 출력
if front < 10:
    print(front, end=' ')
else:
    print(front, end=' ')

if back < 10:
    print(back)
else:
    print(back)