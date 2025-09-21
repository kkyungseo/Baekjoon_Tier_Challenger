import sys

# A, B, N : 입력 (A: 분자, B: 분모, N: 소숫점 아래 N번째 자리)
A, B, N = map(int, sys.stdin.readline().split())

# 나눗셈을 통해 소숫점 아래 N번째 자리수 구하기
# A를 B로 나눈 나머지를 이용해 소숫점 자리수를 계산
# 정수 부분을 제외한 나머지
remainder = A % B  

# 소숫점 아래 N번째 자리수까지 계산
for i in range(N-1):
    remainder = (remainder * 10) % B  # 다음 소숫점 자리수 계산

# N번째 자리수 = (remainder * 10) // B
result = (remainder * 10) // B

print(result)
