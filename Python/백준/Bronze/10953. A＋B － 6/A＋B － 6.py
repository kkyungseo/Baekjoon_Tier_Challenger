import sys

# T : 테스트 케이스의 개수
T = int(input())

for i in range(T):
    # 입력받은 두 숫자 A, B를 콤마(,)로 구분하여 정수로 변환
    A, B = map(int, input().split(','))
    print(A + B)