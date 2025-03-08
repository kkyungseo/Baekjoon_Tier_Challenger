import sys

# A : 경쟁사 제품의 가격
# B : 경쟁사 제품의 성능
# C : 반도체의 가격
A, B, C = map(int, input().split())

print( B // A * 3 * C )
