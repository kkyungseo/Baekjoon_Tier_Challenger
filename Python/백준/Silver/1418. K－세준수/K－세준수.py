import sys

def count_k_sejun_numbers(N, K):
    # 가장 큰 소인수를 저장할 리스트를 초기화
    max_prime_factor = [0] * (N + 1)

    # 에라토스테네스의 체를 응용하여 가장 큰 소인수 기록
    for i in range(2, N + 1):
         # i가 소수일 경우
        if max_prime_factor[i] == 0: 
            # j의 소인수 중 가장 큰 값으로 갱신됨
            for j in range(i, N + 1, i):
                max_prime_factor[j] = i  

    count = 0
                    
    for i in range(1, N + 1):
        if max_prime_factor[i] <= K:
            count += 1

    return count

# 입력
N = int(input())
K = int(input())

# 출력
print(count_k_sejun_numbers(N, K))