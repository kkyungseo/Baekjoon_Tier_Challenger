import sys

# N : 관찰기간
N = int(input())  
# price : 1일차의 초기 가격
price = int(input()) 

# 2일차부터 N일차까지의 변동값
for _ in range(N - 1):  
    change = int(input())  
    price += change  

print(price)  