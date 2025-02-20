# 다이얼의 숫자별 알파멧의 경우 지정
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

S = input()

result = 0

for j in range(len(S)):
    for i in dial:
        if S[j] in i:
            result += dial.index(i)+3
            
print(result)