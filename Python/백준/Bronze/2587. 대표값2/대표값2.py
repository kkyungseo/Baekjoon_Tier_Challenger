import math

# numbers : 입력받는 5개의 정수
numbers = []
for _ in range(5):
    numbers.append(int(input()))

# 평균
average = sum(numbers) // 5

# 중앙값
numbers.sort()       # 오름차순 정렬을 한 후,
median = numbers[2]  # 입력받은 5개의 숫자에서 중앙값인 3번째 값의 인덱스는 2

print(average)
print(median)