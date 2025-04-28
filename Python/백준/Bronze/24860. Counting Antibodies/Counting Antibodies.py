# 입력 받기
V_kappa, J_kappa = map(int, input().split())
V_lambda, J_lambda = map(int, input().split())
V_h, D_h, J_h = map(int, input().split())

# 각각 조합 수 계산
light_kappa = V_kappa * J_kappa
light_lambda = V_lambda * J_lambda
heavy = V_h * D_h * J_h

# 최종 조합 수
total = (light_kappa + light_lambda) * heavy

# 출력
print(total)