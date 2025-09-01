import sys

# emoji : 이모지 입력받기
emoji = input()

# 전체 길이 계산
total_length = len(emoji)

# 콜론의 개수 계산
colon_count = emoji.count(':')

# 언더바의 개수 계산
underscore_count = emoji.count('_')

# 입력 난이도 계산: (전체 길이) + (콜론 개수) + (언더바 개수) × 5
difficulty = total_length + colon_count + underscore_count * 5

print(difficulty)
