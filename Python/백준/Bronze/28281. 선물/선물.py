N, X = map(int, input().split())
A = list(map(int, input().split()))

min_cost = float('inf')

for i in range(N - 1):
    two_day_cost = (A[i] + A[i + 1]) * X
    if two_day_cost < min_cost:
        min_cost = two_day_cost

print(min_cost)