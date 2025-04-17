import sys

def chess_to_coordinates(pos):
    col = ord(pos[0]) - ord('a')  
    row = int(pos[1]) - 1        
    return (col, row)

def find_innohorse_type(a, b):
    x1, y1 = chess_to_coordinates(a)
    x2, y2 = chess_to_coordinates(b)
    
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    # 항상 0 <= x <= y 의 조건 성립
    x, y = sorted((dx, dy))  
    
    return x, y

# 입력
a = input().strip()
b = input().strip()

# 계산
x, y = find_innohorse_type(a, b)

# 출력
print(x, y)