import sys

def main():
    while True:
        n = int(input())
        if n == -1:
            break
        total_distance = 0
        prev_time = 0
        for _ in range(n):
            s, t = map(int, input().split())
            time_diff = t - prev_time
            total_distance += s * time_diff
            prev_time = t
        print(f"{total_distance} miles")

main()