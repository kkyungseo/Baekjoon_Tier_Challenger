import sys

def main():
    # 파이썬이 빠른 입력처리 코드 (생성형AI 참조)
    input = sys.stdin.read
    data = input().splitlines()
    
    N = int(data[0])  # N : 학생의 수
    students = []

    for i in range(1, N + 1):
        X, A, B, C, D = map(int, data[i].split())
        students.append((X, A, B, C, D))

    # 각 과목별로 정렬된 학생 목록
    sorted_korean = sorted(students, key=lambda x: (-x[1], x[0]))  # 국어
    sorted_english = sorted(students, key=lambda x: (-x[2], x[0]))  # 영어
    sorted_math = sorted(students, key=lambda x: (-x[3], x[0]))  # 수학
    sorted_science = sorted(students, key=lambda x: (-x[4], x[0]))  # 과학
    
    # awarded : 상품을 받은 학생 번호를 추적하는 집합
    awarded = set()  
    # result : 과목별 상품을 받은 학생 번호를 저장하는 리스트
    result = [] 

    # 국어, 영어, 수학, 과학 순서대로 1등을 선택
    for sorted_students in [sorted_korean, sorted_english, sorted_math, sorted_science]:
        for student in sorted_students:
            student_num = student[0]
            if student_num not in awarded:
                awarded.add(student_num)
                result.append(student_num)
                break

    # 결과 출력
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
