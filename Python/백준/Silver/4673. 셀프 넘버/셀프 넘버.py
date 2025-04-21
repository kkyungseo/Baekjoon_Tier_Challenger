def d(n):
    return n + sum(map(int, str(n)))

MAX = 10000
generated = set()

for i in range(1, MAX + 1):
    generated.add(d(i))

for i in range(1, MAX + 1):
    if i not in generated:
        print(i)