import sys

s = sys.stdin.readline().strip()
if s:
    n = float(s)
    result = n - 0.3

    # 최대 소수 4자리까지 반올림하여 출력 (불필요한 점 제거하여 출력)
    out = f"{result:.4f}".rstrip("0").rstrip(".")
    print(out)
