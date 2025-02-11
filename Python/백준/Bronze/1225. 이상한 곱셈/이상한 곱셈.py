import sys
input = sys.stdin.readline

A, B = input().split()
A_lst = list(map(int, A))
B_lst = list(map(int, B))

print(sum(A_lst) * sum(B_lst))