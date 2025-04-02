import sys
import math

def count_zeros(N):
    # N! 계산 (문자열로 변환)
    fact = str(math.factorial(N))  
    count = 0

    # 뒤에서부터 0의 개수를 세기 (문자열을 뒤에서부터 인식)
    for i in reversed(fact):
        if i == '0':
            count += 1
        else:
            break
    
    return count

# 입력
N = int(input())
print(count_zeros(N))