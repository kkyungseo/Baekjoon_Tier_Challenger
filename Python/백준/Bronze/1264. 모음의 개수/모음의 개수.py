import sys

# 세야하는 모음 리스트
vowels = "aeiouAEIOU"  

while True:
    S = sys.stdin.readline().strip()  
    if S == "#": 
        break
    count = sum(1 for char in S if char in vowels)  
    print(count)