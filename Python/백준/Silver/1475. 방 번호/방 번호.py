import sys
from collections import Counter

# N: 다솜이의 방 번호 (문자열로 입력받기)
N = input().strip()

# 각 자리의 숫자 세기
ans = [0] * 10

for i in range(len(N)):
    num = int(N[i])
    if num == 6 or num == 9:
        # 6과 9를 같은 세트로 취급
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[num] += 1

print(max(ans))