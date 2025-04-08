import sys

# S, K, H : 입력받는 세 학교의 참여도
S, K, H = map(int, input().split())

if S + K + H >= 100:
    print("OK")
else:
    # 참여도가 가장 낮은 대학명 출력
    min_val = min(S, K, H)
    if min_val == S:
        print("Soongsil")
    elif min_val == K:
        print("Korea")
    else:
        print("Hanyang")