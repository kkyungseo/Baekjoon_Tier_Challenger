S = int(input())  

N = 0
sum_num = 0

# 1부터 N까지의 합이 S를 넘지 않는 최대 N
while sum_num <= S:
    N += 1
    sum_num += N

# sum_num이 S를 초과한 상태로 
# 마지막 N에서 1을 빼는 것으로 조건을 넘지 않는 최대 N 산출
print(N - 1)