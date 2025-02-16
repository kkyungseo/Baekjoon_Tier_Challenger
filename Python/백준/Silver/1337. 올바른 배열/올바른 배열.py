N = int(input())    # N : 배열의 크기

data = sorted([int(input()) for _ in range(N)])

mn = float('inf')

for i in range(N):
    cnt = 0
    for j in range(data[i],data[i]+5):
        if j not in data:
            cnt+=1
    mn = min(mn,cnt)
    
print(mn)
