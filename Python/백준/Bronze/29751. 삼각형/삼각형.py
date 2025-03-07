import sys

# W : 삼각형의 밑변의 길이
# H : 삼각형의 높이의 길이
W, H = map(int, input().split())

result = round(W * H * 1/2, 1)

print(result)