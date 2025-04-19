import sys
import math

R, C, N = map(int, sys.stdin.readline().split())

rows = math.ceil(R / N)
cols = math.ceil(C / N)

print(rows * cols)