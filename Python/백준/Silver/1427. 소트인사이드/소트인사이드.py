import sys

# N: 정렬하려고 하는 수 (정수 변환 없이 문자열 그대로 사용)
N = input().strip()  

# 수의 각 자리수를 내림차순(reverse=True)으로 정렬
digits = sorted(map(int, N), reverse=True)

# 정렬된 숫자들을 이어붙여 출력
print(*digits, sep="")