import sys

# N : 테스트 케이스 입력
N = int(input())

for i in range(N):
    
    # a, b, c : 삼각형 세 변의 길이 입력 (공백 구분)
    a, b, c = map(int, input().split())
    
    # 가장 긴 변 찾기 
    side3 = max(a, b, c)
    
    # 나머지 두 변 구하기
    if side3 == a:
        side1, side2 = b, c
    elif side3 == b:
        side1, side2 = a, c
    else:
        side1, side2 = a, b

    # 직각 삼각형 여부 검사
    if side3**2 == side1**2 + side2**2:
        result = "yes"
    else:
        result = "no"
    
    # 출력 패턴 
    print(f"Scenario #{i+1}:")
    print(result)
    print()  