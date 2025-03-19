import sys
from datetime import date

# 생일 날짜 (연, 월, 일)
n_y, n_m, n_d = map(int, input().split())

# 기준일의 날짜 (연, 월, 일)
d_y, d_m, d_d = map(int, input().split())

# 날짜 객체 생성
birth = date(n_y, n_m, n_d)
d_day = date(d_y, d_m, d_d)

# 만 나이 계산 (생일이 지나지 않았으면 한 살 빼기)
age = d_y - n_y
if (d_m, d_d) < (n_m, n_d):  
    age -= 1

# 세는 나이 계산
counting_age = d_y - n_y + 1

# 연 나이 계산
year_age = d_y - n_y

print(age)          
print(counting_age) 
print(year_age)     