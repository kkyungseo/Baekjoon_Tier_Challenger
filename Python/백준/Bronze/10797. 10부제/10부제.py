import sys

# N : 날짜의 일의 자리 숫자
N = int(input())

# car : 5대의 자동차 번호의 일의 자리 숫자
car = list(map(int, input().split()))

result = car.count(N)

print(result)