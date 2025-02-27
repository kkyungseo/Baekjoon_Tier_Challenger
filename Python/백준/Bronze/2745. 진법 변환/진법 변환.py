N, B = input().split()
array = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]
result = 0

for i,n in enumerate(N):
    result += (int(B)**i)*(array.index(n))
    
print(result)