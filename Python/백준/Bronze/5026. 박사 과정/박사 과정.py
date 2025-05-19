# 입력
n = int(input())

for _ in range(n):
    line = input()
    if line == "P=NP":
        print("skipped")
    else:
        a, b = map(int, line.split('+'))
        print(a + b)