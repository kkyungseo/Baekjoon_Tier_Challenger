import sys

data = sys.stdin.read().strip().splitlines()

n = int(data[0])

student = data[1:1 + n]
correct = data[1 + n:1 + 2 * n]

# s: 학생의 답
# c: 해당 문제의 정답 

# zip으로 쌍을 이뤄 비교(s == c)
# 참인 경우 1을 더해서 합산
print(sum(1 for s, c in zip(student, correct) if s == c))
