import sys

# test_cases : 테스트 케이스의 수 입력받기
test_cases = int(input())

# 각 테스트 케이스 처리
for _ in range(test_cases):
    # 4개의 정수 입력받기: lt, wt, le, we
    # lt, wt: TelecomParisTech 필드의 길이와 너비
    # le, we: Eurecom 필드의 길이와 너비
    lt, wt, le, we = map(int, input().split())
    
    # 각 학교의 스포츠 필드 면적 계산
    telecom_area = lt * wt  # TelecomParisTech 면적
    eurecom_area = le * we  # Eurecom 면적
    
    # 면적 비교하여 결과 출력
    if telecom_area > eurecom_area:
        print("TelecomParisTech")
    elif eurecom_area > telecom_area:
        print("Eurecom")
    else:
        print("Tie")
