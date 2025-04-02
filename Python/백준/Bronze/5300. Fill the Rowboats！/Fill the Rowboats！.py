import sys

# N : 해적의 수
N = int(input())  

for i in range(1, N + 1):
    print(i, end=" ") 

    if i % 6 == 0 or i == N:
        print("Go!", end=" ") 