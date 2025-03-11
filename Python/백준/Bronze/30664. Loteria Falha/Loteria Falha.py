import sys

while True:
    N = input().strip()  
    
    if N == "0":
        break  
    if int(N) % 42 == 0: 
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")
