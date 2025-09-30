import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    h_str, p_str = line.split()

    h = int(h_str)
    p = int(p_str)
    
    print(f"{h / p:.2f}")