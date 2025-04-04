import sys

import math

width, height = map(int, input().split())

# 밭의 면적
field_area = width * height

# 에이커 변환
acres = field_area / 4840

# 씨앗 봉지 개수 계산 
bags_needed = math.ceil(acres / 5)

print(bags_needed)