# 테스트 케이스 개수 입력
n = int(input())

# 테스트 케이스 반복
for _ in range(n):
    x = int(input())
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")