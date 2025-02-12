N = int(input()) 
weather = list(map(int, input().split()))  

current_anger = 0  
total_anger = 0  

for day in weather:
    if day == 1:
        current_anger += 1 
    else:
        current_anger -= 1  
    total_anger += current_anger

print(total_anger)