import sys

result = 0

# 총 4개 구간에서의 이동시간을 차례대로 더해 총 이동시간을 나타냄
for _ in range(4):
	result += int(input())
 
print(result // 60)
print(result % 60)