import sys

# N : 줄의 개수 입력
N = int(input())

for i in range(1, N + 1):
    if i == N:
        # 마지막 줄은 모두 별로 채움
        print('*' * (2 * N - 1))
    else:
        # '공백 + 별 + 중간공백 + 별' 출력 규칙
        spaces = ' ' * (N - i)
        if i == 1:
            print(spaces + '*')
        else:
            middle_spaces = ' ' * (2 * i - 3)
            print(spaces + '*' + middle_spaces + '*')