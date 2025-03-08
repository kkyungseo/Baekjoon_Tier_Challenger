# T : 시간을 의미하는 정수, S : 술의 유무를 나타내는 정수
T, S = map(int, input().split())

if T <= 11:
    # 아침 시간
    sushi_rice = 280
elif 12 <= T <= 16 and S == 0:
    # 점심 시간이고 술이 없는 경우
    sushi_rice = 320
else:
    # 그 외의 경우 (저녁 시간 또는 술과 함께 먹는 경우)
    sushi_rice = 280

print(sushi_rice)