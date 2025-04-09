import sys

kda = input().strip()

# '/'를 기준으로 나눠서 K, D, A로 변환
K, D, A = map(int, kda.split('/'))

if D == 0 or K + A < D:
    print("hasu")
else:
    print("gosu")