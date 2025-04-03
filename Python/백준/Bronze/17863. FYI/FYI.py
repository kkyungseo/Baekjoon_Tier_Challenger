import sys

N = input().strip()

if len(N) == 7 and N[:3] == "555":
    print("YES")
else:
    print("NO")