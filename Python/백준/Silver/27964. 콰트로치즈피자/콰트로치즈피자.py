import sys

# 입력
n = int(input())
toppings = input().split()

# 치즈로 끝나는 토핑만 모은 이후에 중복 제거
cheese_toppings = {topping for topping in toppings if topping.endswith("Cheese")}

# 출력
if len(cheese_toppings) >= 4:
    print("yummy")
else:
    print("sad")