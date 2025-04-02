import sys

# X : 막대기의 길이
X = int(input())  

# 필요한 막대 개수는 X를 이진수로 나타냈을 때 1의 개수와 같음
print(bin(X).count('1'))
