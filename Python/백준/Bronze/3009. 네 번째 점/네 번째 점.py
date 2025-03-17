from collections import Counter

x_list, y_list = [], []

# 직사각형을 구성하는 세 개의 점의 좌표 입력
for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

# 각 좌표 값이 몇 번 등장했는지 세기
x_counter = Counter(x_list)
y_counter = Counter(y_list)

# 한 번만 등장하는 좌표 찾기
for key, value in x_counter.items():
    if value == 1:
        x4 = key
        break

for key, value in y_counter.items():
    if value == 1:
        y4 = key
        break

print(x4, y4)