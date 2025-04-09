import sys

A, B = map(int, input().split())
C = int(input())

# chicken_total_price : 치킨의 가격의 총합
chicken_total_price = 2 * C

# total_balance : 통장 잔고
total_balance = A + B

if total_balance >= chicken_total_price:
    print(total_balance - chicken_total_price)
else:
    print(total_balance)