import sys

# S, T, D : 입력받는 세 정수
# S : 기차의 속도
# T : 파리의 속도
# D : 처음 두 기차 사이의 거리
S, T, D = map(int, input().split())

F = D // (S * 2) * T

print(F)