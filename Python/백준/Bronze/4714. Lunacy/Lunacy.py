import sys

import sys

for line in sys.stdin:
    weight = float(line.strip())

    # 음수가 입력되면 종료 (몸무게는 음수가 될 수 없음)
    if weight < 0:
        break

    moon_weight = weight * 0.167

    print(f"Objects weighing {weight:.2f} on Earth will weigh {moon_weight:.2f} on the moon.")