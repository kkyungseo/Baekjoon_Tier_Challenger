import sys
import math
from collections import Counter

# numbers : 입력받는 숫자들
numbers = [int(input()) for _ in range(10)]

# average : 평균
average = math.floor(math.fsum(numbers) / len(numbers))

# most_common : 최빈값
counter = Counter(numbers)
most_common = counter.most_common(1)[0][0]

print(average)
print(most_common)