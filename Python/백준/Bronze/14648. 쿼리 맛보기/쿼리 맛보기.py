import sys

input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        _, a, b = query
        a -= 1  # 인덱스 보정
        b -= 1
        print(sum(arr[a:b+1]))
        arr[a], arr[b] = arr[b], arr[a]
        
    elif query[0] == 2:
        _, a, b, c, d = query
        a -= 1
        b -= 1
        c -= 1
        d -= 1
        sum1 = sum(arr[a:b+1])
        sum2 = sum(arr[c:d+1])
        print(sum1 - sum2)