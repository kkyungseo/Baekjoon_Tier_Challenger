word = input().upper()
word_list = list(set(word))
result = []

for i in word_list:
    count = word.count(i)
    result.append(count)

if result.count(max(result)) >= 2:
    print("?")
else:
    print(word_list[result.index(max(result))])