import sys

def is_leap_year(year):
    """
    윤년 판별 함수
    
    윤년 규칙:
    1. 400으로 나누어떨어지는 해는 윤년
    2. 4로 나누어떨어지면서 100으로 나누어떨어지지 않는 해는 윤년
    3. 그 외의 경우는 평년
    
    Args:
        year (int): 판별할 연도
        
    Returns:
        bool: 윤년이면 True, 평년이면 False
    """
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def get_days_in_month(month, year):
    """해당 월의 일수 반환 (1월부터 12월까지의 마지막 일수)"""
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[1] = 29
    return days_in_month[month - 1]

def month_to_number(month_str):
    """월 이름을 숫자로 변환"""
    months = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    return months[month_str]

def main():
    # 입력 파싱
    input_line = sys.stdin.readline().strip()
    
    # "MM DD, YYYY HH:MM" 형식 파싱
    parts = input_line.split()
    month_str = parts[0]
    day = int(parts[1].rstrip(','))
    year = int(parts[2])
    time_part = parts[3]
    hour, minute = map(int, time_part.split(':'))
    
    month = month_to_number(month_str)
    
    # 해당 연도의 총 일수 계산
    total_days = 366 if is_leap_year(year) else 365
    
    # 연도 시작부터 현재까지의 일수 계산 (연도 진행률을 계산할 때, 연도 시작부터 현재 시점까지 얼마나 지났는가를 측정)
    days_passed = 0
    for m in range(1, month):
        days_passed += get_days_in_month(m, year)
        # 현재 일은 포함하지 않음 (0부터 시작)
    days_passed += day - 1  
    
    # 현재 일의 시간을 분으로 변환하여 추가
    minutes_passed = days_passed * 24 * 60 + hour * 60 + minute
    
    # 전체 연도의 분 수
    total_minutes = total_days * 24 * 60
    
    # 연도 진행률 계산
    percentage = (minutes_passed / total_minutes) * 100
    
    print(percentage)

if __name__ == "__main__":
    main()
