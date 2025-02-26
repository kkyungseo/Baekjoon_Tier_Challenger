import math

def solve(N):
    fractions = []
    
    # 모든 기약 분수를 찾기 (0/1, 1/1 포함)
    for denominator in range(1, N + 1):
        for numerator in range(0, denominator + 1):
            if math.gcd(numerator, denominator) == 1:  # 기약 분수 여부 확인
                fractions.append((numerator, denominator))
    
    # 기약 분수들을 오름차순 정렬
    fractions.sort(key=lambda x: x[0] / x[1])
    
    # 결과 출력 (총 분수의 개수)
    print(len(fractions))  
    for frac in fractions:
        print(f"{frac[0]}/{frac[1]}")  

# 입력
N = int(input())

# 함수 호출
solve(N)