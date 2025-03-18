import sys
import decimal

# 서브태스크의 정밀도를 충족하기 위해 코드 설정 (1000자리 이상 보장)
# decimal로 임의 정밀도 연산
decimal.getcontext().prec = 1001 

A, B = map(int, sys.stdin.readline().split())

# Decimal을 사용하여 연산 수행
result = decimal.Decimal(A) / decimal.Decimal(B)

# 소수점 이하 1000자리까지 출력
print(result)