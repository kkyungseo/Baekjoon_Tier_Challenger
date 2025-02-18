# A : 앨범에 수록된 곡의 개수 
# I : 평균값 

A, I = map(int, input().split()) 

print ( A * ( I - 1 ) + 1 )