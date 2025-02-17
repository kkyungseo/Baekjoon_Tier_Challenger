import re

T = int(input())  # T : 테스트 케이스 개수

# 정규표현식
pattern = re.compile(r"^[A-F]?A+F+C+[A-F]?$")

"""
^ : 문자열의 시작
[A-F]? : A부터 F까지의 문자가 0개 또는 1개
A+ : A가 1개 이상
F+ : F가 1개 이상
C+ : C가 1개 이상
[A-F]?$ : A부터 F까지의 문자가 0개 또는 1개로 끝남
$ : 문자열의 끝
"""

for _ in range(T):
    chromosome = input().strip()

    if pattern.match(chromosome):
        print("Infected!")
    else:
        print("Good")
