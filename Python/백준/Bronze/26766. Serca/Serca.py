# N : 하트 문양의 출력 반복 횟수
N = int(input())

heart = """ @@@   @@@ 
@   @ @   @
@    @    @
@         @
 @       @ 
  @     @  
   @   @   
    @ @    
     @     """

# 하트 모양을 N번 출력
for _ in range(N):
    print(heart)