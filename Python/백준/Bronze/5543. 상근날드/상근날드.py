import sys

arr = [int(input()) for _ in range(5)]

burger_min = min(arr[:3])
soda_min = min(arr[3:])

result = burger_min + soda_min - 50

print(result)