def solve_polyomino(board):
    """
    X를 AAAA 또는 BB로 덮는 함수 (사전순으로 가장 앞서는 답을 반환)
    """
    result = []
    i = 0
    
    while i < len(board):
        if board[i] == '.':
            result.append('.')
            i += 1
        else:
            # 연속된 X의 개수 세기 (연속된 X그룹 분석)
            x_count = 0
            while i < len(board) and board[i] == 'X':
                x_count += 1
                i += 1
            
            # X가 홀수 개면 덮을 수 없음 (AAAA=4개, BB=2개로만 구성됨)
            if x_count % 2 == 1:
                return -1
            
            # 사전순으로 앞서려면 AAAA를 최대한 많이 사용해야 함 
            # AAAA는 4개씩, BB는 2개씩
            aaaa_count = x_count // 4
            bb_count = (x_count % 4) // 2
            
            # AAAA와 BB를 결과에 추가
            result.extend(['A'] * (aaaa_count * 4))
            result.extend(['B'] * (bb_count * 2))
    
    return ''.join(result)

# 입력 받기
board = input().strip()

# 결과 계산
result = solve_polyomino(board)

# 출력
print(result)
