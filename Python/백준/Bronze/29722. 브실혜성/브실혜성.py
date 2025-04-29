def to_days(year, month, day):
    return year * 360 + (month - 1) * 30 + (day - 1)

def from_days(total_days):
    year = total_days // 360
    total_days %= 360
    month = total_days // 30 + 1
    day = total_days % 30 + 1
    return f"{year:04d}-{month:02d}-{day:02d}"

# 입력
today = input().strip()
N = int(input())

# 날짜 파싱
yyyy, mm, dd = map(int, today.split('-'))

# 날짜 계산
today_days = to_days(yyyy, mm, dd)
future_days = today_days + N

# 결과 출력
print(from_days(future_days))