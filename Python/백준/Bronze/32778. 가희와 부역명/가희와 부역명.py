station_info = input().strip()

# 케이스 1 : 괄호 '('가 있는 경우 부역명이 있는 경우
if '(' in station_info and ')' in station_info:
    start = station_info.index('(')
    end = station_info.index(')')
    
    station_name = station_info[:start].strip()
    sub_station_name = station_info[start+1:end].strip()
else:
    # 케이스 2 : 부역명이 없는 경우
    station_name = station_info
    sub_station_name = '-'

print(station_name)
print(sub_station_name)