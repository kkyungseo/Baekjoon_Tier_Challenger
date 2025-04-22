import sys
input = sys.stdin.read

# 입력 전체 읽고, 줄 단위로 나누기
data = input().split()

# 입력 처리
# 숫자 카드의 개수
N = int(data[0])  
# 상근이 숫자카드 집합
sanggeun_cards = set(map(int, data[1:N+1]))  

# 체크할 숫자의 개수
M = int(data[N+1])  
# 체크할 숫자들
check_cards = map(int, data[N+2:])  

# 결과 출력
result = []
for card in check_cards:
    if card in sanggeun_cards:
        result.append("1")
    else:
        result.append("0")

print(' '.join(result))