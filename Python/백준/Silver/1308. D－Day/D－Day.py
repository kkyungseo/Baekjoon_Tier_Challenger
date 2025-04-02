import sys
from datetime import date

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def d_day(y1, m1, d1, y2, m2, d2):
    if (y2 > y1 + 1000) or (y2 == y1 + 1000 and (m2 > m1 or (m2 == m1 and d2 >= d1))):
        print("gg")
        return
    
    # 날짜 객체 생성 후 차이 계산
    start_date = date(y1, m1, d1)
    end_date = date(y2, m2, d2)
    diff = (end_date - start_date).days
    
    print(f"D-{diff}")

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

d_day(y1, m1, d1, y2, m2, d2)