import sys

# M : 입력받는 월
M = int(input())
# D : 입력받는 일
D = int(input())

if M < 2:  
    print("Before")
elif M == 2: 
    if D == 18:  
        print("Special")
    elif D > 18:  
        print("After")
    else: 
        print("Before")
else:  
    print("After")