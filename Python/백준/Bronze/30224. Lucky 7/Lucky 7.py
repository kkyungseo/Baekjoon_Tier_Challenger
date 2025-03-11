import sys

# N : 입력받는 정수
N = int(input())

contains_seven = '7' in str(N)

divisible_by_seven = N % 7 == 0

if contains_seven and divisible_by_seven:
    print(3)
elif contains_seven:
    print(2)
elif divisible_by_seven:
    print(1)
else:
    print(0)