import sys

# speed_limit : 제한 속도 입력
speed_limit = int(input())  
# recorded_speed : 차량 속도 입력
recorded_speed = int(input()) 

over_speed = recorded_speed - speed_limit  

if over_speed <= 0:
    print("Congratulations, you are within the speed limit!")
elif 1 <= over_speed <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= over_speed <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")