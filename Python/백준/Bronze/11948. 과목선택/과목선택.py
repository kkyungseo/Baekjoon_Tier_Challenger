def max_exam_score():

    scores = [int(input()) for _ in range(6)]
    
    # 과학 4과목 중 상위 3개 선택
    science_scores = sorted(scores[:4], reverse=True)[:3]
    # 역사, 지리 중 높은 점수 선택
    social_score = max(scores[4], scores[5])
    
    # 총점 계산 및 출력
    print(sum(science_scores) + social_score)

max_exam_score()