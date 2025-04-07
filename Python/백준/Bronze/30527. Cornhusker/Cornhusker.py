import sys

# 입력: 5개의 이삭에 대한 A, L 값 (총 10개 정수)
data = list(map(int, input().split()))

# A, L 값으로부터 각 이삭의 낱알 수 계산
kernel_counts = []
for i in range(0, 10, 2):
    A = data[i]
    L = data[i + 1]
    kernel_counts.append(A * L)

# avg_kernels_per_ear : 평균 낱알 수
avg_kernels_per_ear = sum(kernel_counts) // 5

# 두 번째 줄 입력: 구간 내 이삭 수 N, KWF
N, KWF = map(int, input().split())

# 총 낱알 수 = 평균 낱알 수 × 이삭 수
total_kernels = avg_kernels_per_ear * N

# 예상 부셸 수
bushels_per_acre = total_kernels // KWF

# 출력
print(bushels_per_acre)