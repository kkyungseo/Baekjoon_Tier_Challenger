import math

try:
    X = float(input().strip())
    result = math.floor(X)
    print(result)
    
except ValueError:
    print("")