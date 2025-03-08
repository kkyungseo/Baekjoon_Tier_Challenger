import sys

# bits : 입력받은 수를 리스트로 저장
bits = list(map(int, input().split()))

print("F" if 9 in bits else "S")