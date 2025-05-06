import sys

# N : 용의자 수
N = int(input())  
# 용의자 이름들 입력받기
suspects = [input().strip() for _ in range(N)]  

for name in suspects:
    if 'S' in name:
        print(name)
        # 정답은 항상 유일하므로 찾으면 바로 종료
        break  