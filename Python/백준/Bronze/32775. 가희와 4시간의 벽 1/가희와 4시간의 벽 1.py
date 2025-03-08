import sys

# S : 고속철도 이용 시간 (역 ~ 역)
S = int(input())
# F : 이동시간 (공항 ~ 공항)
F = int(input())

if S <= F :
    print("high speed rail")
else :
    print("flight")
