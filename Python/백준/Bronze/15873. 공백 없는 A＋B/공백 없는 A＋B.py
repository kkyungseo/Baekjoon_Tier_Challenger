import sys

n = input()

# 입력이 4자리라면 A=10, B=10 → 10 + 10 = 20
if len(n) == 4:           # 예: 1010
    print(20)

# 입력이 2자리라면 A, B가 둘 다 한 자리 수 → 각 자리를 더함
elif len(n) == 2:         # 예: 23 → 2 + 3 = 5
    print(int(n[0]) + int(n[1]))

# 입력이 3자리인 경우
else:
    # 뒷자리가 0이면 B = 10 → A는 한 자리 수 (예: 310 → 3 + 10)
    if int(n[-1]) == 0:   # 예: 910 → 9 + 10 = 19
        print(int(n[0]) + 10)
    else:                 # 앞 2자리가 10이면 A = 10, B는 한 자리 수 (예: 105 → 10 + 5)
        print(int(n[-1]) + 10)
