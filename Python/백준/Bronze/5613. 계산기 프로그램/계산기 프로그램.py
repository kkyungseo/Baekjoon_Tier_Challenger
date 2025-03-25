import sys

# result : 연결되어 남는 계산결과
result = int(input())

while True:
    # S : 입력되는 연산자
    S = input()
    if S == "=":
        break
    # N : 입력되는 숫자
    N = int(input())
    if S == "+":
        result += N
    elif S == "-":
        result -= N
    elif S == "*":
        result *= N
    elif S == "/":
        result //= N
        
print(result)