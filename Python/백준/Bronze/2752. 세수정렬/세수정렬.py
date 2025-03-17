import sys

# num : 입력받는 정수 리스트 (3개로 제한)
num = list(map(int, input().split()))

# 3개의 정수가 입력되었는지 확인
if len(num) == 3:
    # 리스트를 오름차순으로 정렬
    num.sort()
    
    print(num[0])
    print(num[1])
    print(num[2])
    
else:
    print(" ")