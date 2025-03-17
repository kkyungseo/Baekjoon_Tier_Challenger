import sys

while True :
    try :
        print(input())
    # 더 이상 입력받는 데이터가 없는 경우에 break
    except EOFError:
        break