import sys

containers = list(map(int, sys.stdin.readline().split()))

total_containers = sum(containers)

refund_amount = total_containers * 5

print(refund_amount)