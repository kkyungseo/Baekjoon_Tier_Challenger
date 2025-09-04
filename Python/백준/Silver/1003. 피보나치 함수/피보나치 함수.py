import sys

# t : 테스트 케이스의 수
t = int(input())

# 각 숫자별로 0과 1이 출력되는 횟수를 저장하는 딕셔너리
# memo[n] = (0이 출력되는 횟수, 1이 출력되는 횟수) 
# 공백을 두고 출력하기
memo = {}

def fibonacci_count(n):
    if n in memo:
        return memo[n]
    
    if n == 0:
        memo[n] = (1, 0)  # 0이 1번, 1이 0번 출력
        return memo[n]
    elif n == 1:
        memo[n] = (0, 1)  # 0이 0번, 1이 1번 출력
        return memo[n]
    else:
        # fibonacci(n-1)과 fibonacci(n-2)의 결과를 합산
        count1 = fibonacci_count(n-1)
        count2 = fibonacci_count(n-2)
        memo[n] = (count1[0] + count2[0], count1[1] + count2[1])
        return memo[n]

# 각 테스트 케이스 처리
for _ in range(t):
    n = int(input())
    zero_count, one_count = fibonacci_count(n)
    print(zero_count, one_count)
