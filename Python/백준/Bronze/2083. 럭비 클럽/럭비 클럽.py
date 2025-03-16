import sys

while True:
    person = input().split()

    if person[0] == "#":
        break

    # 입력받은 정보 분리
    name = person[0]
    age = int(person[1])  
    weight = int(person[2]) 

    if age > 17 or weight >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")