import sys

# isbn_prefix : ISBN의 고정된 첫 10자리 숫자
isbn_prefix = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]

# 마지막 3자리 숫자 입력받기
isbn_suffix = [int(input()) for _ in range(3)]

# 전체 13자리 ISBN 리스트 생성
isbn = isbn_prefix + isbn_suffix

# one_three_sum : 1-3-sum 계산
one_three_sum = sum(num * (1 if i % 2 == 0 else 3) for i, num in enumerate(isbn))

print(f"The 1-3-sum is {one_three_sum}")