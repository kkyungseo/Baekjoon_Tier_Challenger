# N : 바구니의 개수
# M : 순서를 바꾸는 횟수
N, M = map(int, input().split())

# 바구니 번호 초기화 ( 1 ~ N )
basket = list(range(1, N + 1))

# 바구니의 순서 변경 
for _ in range(M):
    i, j = map(int, input().split())
    # i에서 j까지 역순으로 변경 
    basket[i-1:j] = reversed(basket[i-1:j])

# 출력 ( *로 공백구분 )
print(*basket)