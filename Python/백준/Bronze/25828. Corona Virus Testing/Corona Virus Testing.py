# 입력
g, p, t = map(int, input().split())

# 방법 1 : 모두 개별 테스트
individual_tests = g * p

# 방법 2 : 그룹 테스트 & 양성 그룹 개별 테스트
group_tests = g + (t * p)

# 출력
if individual_tests < group_tests:
    print(1)
elif individual_tests > group_tests:
    print(2)
else:
    print(0)