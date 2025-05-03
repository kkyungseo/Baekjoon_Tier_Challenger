# 대기 중인 사람의 위치 입력
x, y = map(int, input().split())

# 택시 수 입력
n = int(input())

# 가장 가까운 거리와 택시 위치 초기화
min_distance = float('inf')
closest_taxi = (0, 0)

# 택시 위치들을 하나씩 입력받고 거리 계산
for _ in range(n):
    tx, ty = map(int, input().split())
    distance = abs(x - tx) + abs(y - ty)
    
    if distance < min_distance:
        min_distance = distance
        closest_taxi = (tx, ty)

# 가장 가까운 택시 위치 출력
print(closest_taxi[0], closest_taxi[1])