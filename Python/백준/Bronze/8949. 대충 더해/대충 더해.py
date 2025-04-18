import sys

# A, B : 입력받는 두 정수
A, B = map(int, input().split())

# A, B를 문자열로 변환
strA = str(A)
strB = str(B)

# 자릿수를 맞추기 위해 두 문자열의 길이를 맞추기
max_len = max(len(strA), len(strB))

# 길이가 더 작은 문자열에 앞에 0을 채워서 길이 맞추기
strA = strA.zfill(max_len)
strB = strB.zfill(max_len)

# result : 결과를 저장할 빈 리스트
result = []

# 각 자리 수를 더해서 결과 리스트에 추가
for i in range(max_len):
    digit_sum = int(strA[i]) + int(strB[i])
    result.append(str(digit_sum))

# 공백 없이 출력
print(''.join(result))