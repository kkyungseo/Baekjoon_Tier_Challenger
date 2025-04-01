def time_diff(h1, m1, s1, h2, m2, s2):
    # 출근 시간과 퇴근 시간의 차이를 계산
    start_seconds = h1 * 3600 + m1 * 60 + s1
    end_seconds = h2 * 3600 + m2 * 60 + s2
    diff_seconds = end_seconds - start_seconds
    
    # 계산된 초를 다시 시, 분, 초로 변환
    hours = diff_seconds // 3600
    diff_seconds %= 3600
    minutes = diff_seconds // 60
    seconds = diff_seconds % 60
    
    return hours, minutes, seconds

# 입력 받기
for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    hours, minutes, seconds = time_diff(h1, m1, s1, h2, m2, s2)
    print(hours, minutes, seconds)