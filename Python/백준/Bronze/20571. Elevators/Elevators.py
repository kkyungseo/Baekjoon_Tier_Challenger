zoning, N = input().split()
N = int(N)

# (최대 층수, 필요한 엘리베이터 개수) 튜플 구조 
elevator_requirements = {
    "residential": [(1, 0), (5, 1), (10, 2), (15, 3), (20, 4)],
    "commercial": [(1, 0), (7, 1), (14, 2), (20, 3)],
    "industrial": [(1, 0), (4, 1), (8, 2), (12, 3), (16, 4), (20, 5)],
}

for max_floor, elevators in elevator_requirements[zoning]:
    if N <= max_floor:
        print(elevators)
        break
