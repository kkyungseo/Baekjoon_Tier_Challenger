# N : 더할 숫자의 개수
n = int(input())
total = 0  # 합계 저장
count = 0  # 처리한 숫자의 개수

while count < n:
    num = int(input())
    total += num
    count += 1

print(total)