# A, B : 상근이가 적은 두 수
# 문자열로 입력 받기
A, B = input().split()  

# 세 자리 숫자만 입력받기
if len(A) == 3 and len(B) == 3:  
    # A, B를 거꾸로 뒤집어(::-1) 정수 rev_A, rev_B로 변환
    rev_A = int(A[::-1])  
    rev_B = int(B[::-1])  
    # 최댓값 출력 
    print(max(rev_A, rev_B))
else:
    print("숫자를 다시 입력하세요.")