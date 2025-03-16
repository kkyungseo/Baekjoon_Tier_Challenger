import sys

# 연산자와 입력되는 수 정보 입력
a, _, b, _, c = input().split()

if int(a) + int(b) == int(c) : 
    print("YES")
else : 
    print("NO")