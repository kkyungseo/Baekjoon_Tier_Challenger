N, B = map(int, input().split())

S = ''
array = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N:
    S += str(array[N%B])
    N //= B

print(S[::-1])