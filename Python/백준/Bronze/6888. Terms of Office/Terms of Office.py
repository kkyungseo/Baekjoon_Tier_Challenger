import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    X = int(data[0])
    Y = int(data[1]) if len(data) > 1 else X

    # 동시에 직책자가 변하는 주기는 최소공배수(LCM)로 계산가능
    LCM = 60

    results = []

    # 연도 구간은 X부터 Y "포함"이므로, 파이썬의 range가 끝값을 제외하는 특성상 range(X, Y + 1)을 사용
    # 각 해에 대해 (year - X) % LCM == 0 이면 X에서부터 정확히 60의 배수에 해당하는 해만 선별됨

    for year in range(X, Y + 1):
        if (year - X) % LCM == 0:
            results.append(f"All positions change in year {year}")

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()
