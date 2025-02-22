# N : 입력받는 수
N = int(input())

line = 0
line_end_num = 0

# 속한 라인 확인
while line_end_num < N: 
    line += 1
    line_end_num += line

# K : 마지막 수와 주어진 수의 차
K = line_end_num - N 

# 짝수, 홀수의 경우 
if line % 2 == 0:
    a = line - K
    b = K + 1
else:
    a = K + 1
    b = line - K

# 정수 형태인 a, b를 문자열로 바꾸어 출력
print(str(a) + '/' + str(b))