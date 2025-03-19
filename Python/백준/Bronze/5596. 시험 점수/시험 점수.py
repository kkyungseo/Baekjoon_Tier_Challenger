import sys

# scr1 : 민국의 점수
# scr2 : 만세의 점수
scr1 = list(map(int, input().split()))
scr2 = list(map(int, input().split()))

# sum() 함수는 리스트에 대해서 직접 호출해야 하므로 () 제거
result1 = sum(scr1)
result2 = sum(scr2)

# 더 높은 점수를 출력
print(max(result1, result2))