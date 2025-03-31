import sys

# 문자 변환 테이블 
trans_table = str.maketrans('ieIE', 'eiEI')

# 입력 받기
input_lines = sys.stdin.read().splitlines()

# 각 줄을 변환하여 출력
for line in input_lines:
    print(line.translate(trans_table))