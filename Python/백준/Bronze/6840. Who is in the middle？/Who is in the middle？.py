import sys

# A, B, C : 세 그릇의 무게 
A = int(input())
B = int(input())
C = int(input())

weights = [A, B, C]
weights.sort()
print(weights[1])