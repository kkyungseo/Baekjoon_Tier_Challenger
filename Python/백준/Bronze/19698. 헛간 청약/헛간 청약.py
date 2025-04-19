import sys

# N : 소의 수
# W * H : 직사각형 모양의 헛간
# L : 소들에게 배정되는 공간의 크기

N, W, H, L = map(int, input().split())

space = (W // L) * (H // L) 

print(min(N, space))