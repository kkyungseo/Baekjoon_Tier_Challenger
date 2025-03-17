import sys

# num : 입력되는 숫자들의 리스트
num = list(map(int, input().split()))

num.sort()

# 총 3개의 수이므로, 리스트에서 인덱스가 1인 경우가 두 번째 크기의 숫자가 됨
print(num[1])