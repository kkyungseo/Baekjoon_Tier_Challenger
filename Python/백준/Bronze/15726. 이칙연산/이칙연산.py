import sys

# A, B, C : 입력받는 세 정수
A, B, C = map(int, input().split())

result1 = int(A / B * C)
result2 = int(A * B / C)

if result1 > result2 :
    print(result1)
elif result1 < result2 :
    print(result2)
else :
    pass