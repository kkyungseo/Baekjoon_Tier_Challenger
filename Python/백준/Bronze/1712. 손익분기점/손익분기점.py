import sys

# A : 고정비용
# B : 가변비용
# C : 책정된 가격
A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print(int(A//(C-B)+1))