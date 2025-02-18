N = int(input())        # N : 집의 수
cost = []               # cost : 각 집의 색칠 비용 

# 각 집의 페인트 비용 입력받기
for _ in range(N):
    cost.append(list(map(int, input().split())))

# 초기화
INF = float('inf')
min_cost = INF

# 1번 집의 색깔을 각각 빨강(0), 초록(1), 파랑(2)으로 고정하고 시도
for first_color in range(3):
    # DP 테이블 초기화
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][first_color] = cost[0][first_color]  # 1번 집의 색 고정
    
    # 2번 집부터 N번 집까지 DP 갱신
    for i in range(1, N):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])  # 빨강
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])  # 초록
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])  # 파랑
    
    # 마지막 집의 색깔이 처음 집의 색깔과 같으면 안 됨
    for last_color in range(3):
        if last_color != first_color:
            min_cost = min(min_cost, dp[N-1][last_color])

# 최소 비용 출력
print(min_cost)