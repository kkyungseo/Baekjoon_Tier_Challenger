import sys

for line in sys.stdin:
    
    # N : 입력받는 정수 (float로 실수 변환)
    N = float(line.strip())
    
    if N == 0:
        break

    total = 1 + N + N**2 + N**3 + N**4
    
    print(f"{total:.2f}")