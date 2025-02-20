while True:
    number = input().strip()  
    if number == "#":         # 종료 조건 확인
        break

    weighted_sum = 0          # 가중치가 적용된 합을 저장
    length = len(number)      # 숫자의 길이

    # 가중치를 곱하여 합 구하기
    for i in range(length):
        digit = int(number[length - 1 - i]) 
        weight = i + 2                  # 가중치 계산 (2부터 시작)
        weighted_sum += digit * weight  # 가중치를 곱한 값을 더하기

    remainder = weighted_sum % 11  
    check_digit = 11 - remainder  # 체크 숫자 계산

    # 체크 숫자가 10이면 "Rejected", 11이면 "0", 그 외는 그대로 출력
    if check_digit == 10:
        result = "Rejected"
    elif check_digit == 11:
        result = "0"
    else:
        result = str(check_digit)

    print(number, "->", result)  
