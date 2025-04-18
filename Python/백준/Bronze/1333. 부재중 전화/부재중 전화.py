import sys

# N, L, D : 입력받는 세 정수
N, L, D = map(int, input().split())

# N : 총 노래의 개수
# L : 모든 노래의 길이
# D : 전화벨이 울리는 주기 

# (노래와 노래 사이에는 5초 동안 노래가 나오지 않는 조용한 구간이 있음)

# 노래가 재생되는 구간을 true로 표시하는 배열
# 앨범이 재생되는 총 시간은 (L + 5) * (N - 1) + L
album_time = (L + 5) * (N - 1) + L
playing = [False] * (album_time)

# 각 노래의 재생 구간에 대한 True 표시
for i in range(N):
    start = i * (L + 5)
    end = start + L
    for t in range(start, end):
        playing[t] = True

# D초마다 전화벨이 울리므로, 0초부터 확인
t = 0
while True:
    # 전화벨은 1초 동안 울리므로, t부터 t+1까지 확인
    if t >= album_time or not playing[t]:
        # 전화벨이 들릴 수 있는 가장 빠른 시점
        print(t)
        break
    t += D
