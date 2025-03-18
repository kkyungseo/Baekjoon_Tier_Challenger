import sys

# 비트마스크를 활용한 집합 연산 수행
S = 0  

# M : 입력받는 연산의 개수
M = int(sys.stdin.readline().strip())  

for _ in range(M):
    command = sys.stdin.readline().strip().split()
    
    if command[0] == "add":
        x = int(command[1])
        S |= (1 << x)  
    
    elif command[0] == "remove":
        x = int(command[1])
        S &= ~(1 << x)  
    
    elif command[0] == "check":
        x = int(command[1])
        print(1 if S & (1 << x) else 0) 
    
    elif command[0] == "toggle":
        x = int(command[1])
        S ^= (1 << x)  
    
    elif command[0] == "all":
        S = (1 << 21) - 1  
    
    elif command[0] == "empty":
        S = 0 
