import sys

# S : 입력받은 문자열
S = input()

for i in S:
    if i.isupper() == True:
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")