import sys

T = int(input())  

for _ in range(T):
    # 첫 번째 이진수
    a = input().strip()  
    # 두 번째 이진수
    b = input().strip()  

    # 해밍 거리 계산 : 각 자리 비교해서 다르면 +1
    hamming_distance = sum(1 for x, y in zip(a, b) if x != y)

    # 출력
    print(f"Hamming distance is {hamming_distance}.")