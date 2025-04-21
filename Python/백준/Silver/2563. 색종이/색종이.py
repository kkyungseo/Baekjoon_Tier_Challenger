# 100x100 도화지를 0으로 초기화하여 면적과 넓이에 대한 값을 초기화
paper = [[0] * 100 for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
        
    # 색종이의 영역을 1로 표시하여 넓이 계산이 가능하게 만듦
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

# 검은 영역의 넓이는 위의 설정에 따라서 1의 개수를 세면 넓이가 나오게 됨
black_area = sum(map(sum, paper))
print(black_area)