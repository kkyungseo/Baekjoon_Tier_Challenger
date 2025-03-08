import math

try:
    # N : 입력되는 연도
    N = int(input())  
    result = abs(N - 2024)
    print(result)
    
except ValueError:
    print("")
