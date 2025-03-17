import sys

# scores : 학생들의 점수를 담을 리스트
scores = []

# 점수 입력받기 (5명)
for _ in range(5):
    N = int(input())
    # 40점 미만이면 40점으로 처리, 40점 이상이면 입력된 값을 사용
    if N < 40:
        scores.append(40)
    else:
        scores.append(N)

# 평균 점수 계산
average = sum(scores) // 5

# 출력
print(average)