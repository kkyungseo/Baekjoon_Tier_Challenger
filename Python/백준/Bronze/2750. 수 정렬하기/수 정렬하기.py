import sys

# N : 주어지는 숫자의 개수
N = int(input())

# numbers : 입력받은 숫자들의 리스트
numbers = [int(input()) for _ in range(N)]  

numbers.sort()

for num in numbers:
    print(num)