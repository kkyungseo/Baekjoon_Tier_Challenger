import sys

def print_numbers_between(A, B):
    if A > B:
        # A가 B보다 크다면 두 값을 교환할 수 있도록 설정
        A, B = B, A  
        
    # numbers : A와 B 사이의 정수 리스트
    numbers = list(range(A + 1, B))  
    
    # 개수 출력
    print(len(numbers))
    # 정수들 출력
    if numbers:
        print(*numbers)  

# 사용자 입력 받기
A, B = map(int, input().split())

print_numbers_between(A, B)