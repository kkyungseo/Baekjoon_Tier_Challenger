N = int(input())

for _ in range(N):
	money = int(input())
	for i in [25, 10, 5, 1]:
		print(money // i, end = ' ')
		money = money % i