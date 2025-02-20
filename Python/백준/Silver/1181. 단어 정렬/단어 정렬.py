# N : 입력
N = int(input())

words = [str(input()) for i in range(N)]

words = list(set(words))
words.sort()
words.sort(key=len)

for i in words:
    print(i)