import sys

# T : 입력 받는 테스트 케이스의 수 
T = int(input())

for case_num in range(1, T + 1):
    sacks = list(map(int, input().split()))
    # 최댓값 출력되도록 설정
    max_weight = max(sacks)
    # 출력 방식 설정
    print(f"Case #{case_num}: {max_weight}")