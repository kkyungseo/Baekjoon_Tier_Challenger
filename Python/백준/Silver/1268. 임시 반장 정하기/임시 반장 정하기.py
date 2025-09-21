import sys

# n : 학생 수 (3 <= n <= 1000)
n = int(sys.stdin.readline())

# students : 각 학생의 1학년부터 5학년까지 반 정보, n x 5 행렬로 작성
students = []
for i in range(n):
    student = list(map(int, sys.stdin.readline().split()))
    students.append(student)

# 각 학생별로 같은 반이었던 학생 수 계산
# 현재까지 찾은 최대 "같은 반이었던 학생 수"를 저장하는 변수
max_count = -1
# 현재까지 임시 반장으로 선정된 학생의 번호를 저장하는 변수
class_leader = 1

# i번 학생
for i in range(n):  
    same_class_students = set()  # 같은 반이었던 학생들 (중복 제거)
    
    for grade in range(5):  # 1학년부터 5학년까지
        current_class = students[i][grade]
        
        for j in range(n):  # 다른 학생들과 비교
            if i != j and students[j][grade] == current_class:
                same_class_students.add(j)
    
    # 같은 반이었던 학생 수가 현재 최대값보다 크면 업데이트
    if len(same_class_students) > max_count:
        max_count = len(same_class_students)
        class_leader = i + 1  # 학생 번호는 1부터 시작

print(class_leader)
