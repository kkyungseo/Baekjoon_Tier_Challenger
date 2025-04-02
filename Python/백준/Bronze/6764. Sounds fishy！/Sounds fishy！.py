import sys

depth1 = int(input())
depth2 = int(input())
depth3 = int(input())
depth4 = int(input())

# 입력받은 깊이 값을 리스트로 저장
depths = [depth1, depth2, depth3, depth4]

if depths[0] < depths[1] < depths[2] < depths[3]:
    print("Fish Rising")
elif depths[0] > depths[1] > depths[2] > depths[3]:
    print("Fish Diving")
elif depths[0] == depths[1] == depths[2] == depths[3]:
    print("Fish At Constant Depth")
else:
    print("No Fish")