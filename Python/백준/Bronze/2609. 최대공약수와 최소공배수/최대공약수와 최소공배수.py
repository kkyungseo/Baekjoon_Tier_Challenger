import math

# A, B : 입력되는 두 개의 자연수
A, B = map(int, input().split())

# gcd : 최대공약수
gcd = math.gcd(A, B)
# lcm : 최소공배수
lcm = (A * B) // gcd

print(gcd)
print(lcm)