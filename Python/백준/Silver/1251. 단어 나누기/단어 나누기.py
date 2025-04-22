import sys

# 입력 정리
word = input()
results = []

# i : 첫 번째 부분의 끝 인덱스
# j : 두 번째 부분의 끝 인덱스
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        part1 = word[:i][::-1]
        part2 = word[i:j][::-1]
        part3 = word[j:][::-1]
        combined = part1 + part2 + part3
        results.append(combined)

# 사전순 정렬 후 가장 앞에 있는 단어 출력
print(min(results))