import sys

a, b, c = map(int, input().split())

if a == b == c:
    print(2)  
else:
    sides = sorted([a, b, c])
    if sides[0] + sides[1] > sides[2]:
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            print(1)  
        else:
            print(0)  
    else:
        print(0) 