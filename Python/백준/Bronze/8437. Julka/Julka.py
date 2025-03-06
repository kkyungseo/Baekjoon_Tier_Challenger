total_apples = int(input())  
difference = int(input())  

# N : Natalia가 가진 사과의 수 계산
N = (total_apples - difference) // 2

# K : Klaudia가 가진 사과의 수 계산
K = N + difference

# 결과 출력
print(K)
print(N)