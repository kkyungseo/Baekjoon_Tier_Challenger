import sys

def calculate_score(T, F, S, P, C):
    return (T * 6) + (F * 3) + (S * 2) + (P * 1) + (C * 2)

visitor = list(map(int, sys.stdin.readline().split()))
home = list(map(int, sys.stdin.readline().split()))

visitor_score = calculate_score(*visitor)
home_score = calculate_score(*home)

print(visitor_score, home_score)