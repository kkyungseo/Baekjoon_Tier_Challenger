import sys

# original : 원래 문자열
original = "UAPC"

# 입력
s = input()

# removed : 결과를 저장할 빈 문자열
removed = ""

# i : s에서 몇 번째 문자를 확인 중인지 저장할 변수 (반복문에서 활용) 
i = 0

# original의 각 문자를 하나씩 확인
for ch in original:
    # 아직 s를 다 보지 않았고, original의 현재 문자가 s의 현재 문자와 같으면
    if i < len(s) and ch == s[i]:
        # s의 다음 문자를 보기 위해 인덱스를 1 증가시킴
        i += 1
    else:
        # 문자가 s에 없으면 제거된 문자이므로 결과에 추가
        removed += ch

# 출력
print(removed)