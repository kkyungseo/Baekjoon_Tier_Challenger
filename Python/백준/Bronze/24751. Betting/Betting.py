import sys

# N : 입력받는 정수
N = int(input())

ratio1 = 100 / N
ratio2 = 100 / (100 - N)

print(f"{ratio1:.10f}")
print(f"{ratio2:.10f}")