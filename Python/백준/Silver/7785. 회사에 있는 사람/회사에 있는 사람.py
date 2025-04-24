# 입력
n = int(input())
log = set()


for _ in range(n):
    name, action = input().split()
    if action == 'enter':
        log.add(name)
    elif action == 'leave':
        # discard는 존재하지 않아도 에러 없이 제거하기 위해 작성
        log.discard(name)  

# 현재 회사에 남아 있는 사람들을 오름차순으로 출력
for name in sorted(log, reverse=True):
    print(name)