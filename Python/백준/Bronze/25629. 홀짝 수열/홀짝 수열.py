import sys

def can_form_odd_even_sequence(n, sequence):
    # 홀수와 짝수 분리 및 정렬
    odd_numbers = sorted([x for x in sequence if x % 2 == 1])
    even_numbers = sorted([x for x in sequence if x % 2 == 0])

    odd_index, even_index = 0, 0
    result_sequence = []

    for i in range(n):
        if i % 2 == 0:  # 1-based 기준으로 홀수 번째 위치
            if odd_index >= len(odd_numbers):
                return 0
            result_sequence.append(odd_numbers[odd_index])
            odd_index += 1
        else:  # 짝수 번째 위치
            if even_index >= len(even_numbers):
                return 0
            result_sequence.append(even_numbers[even_index])
            even_index += 1

    return 1  # 조건을 만족하는 수열 생성 가능

# 입력
n = int(input())
sequence = list(map(int, input().split()))
print(can_form_odd_even_sequence(n, sequence))