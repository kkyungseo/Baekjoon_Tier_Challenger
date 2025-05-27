N = int(input())

# 첫 번째 피갤컵
year = 2024
month = 8

# (N - 1)번 7개월씩 더함
months_to_add = (N - 1) * 7

# 총 개월 수를 기준으로 연도와 월 계산
month += months_to_add
year += (month - 1) // 12
month = (month - 1) % 12 + 1

print(year, month)