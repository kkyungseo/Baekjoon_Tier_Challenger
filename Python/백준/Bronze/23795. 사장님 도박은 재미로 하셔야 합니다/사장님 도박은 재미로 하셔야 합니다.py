import sys

total = 0

while True:
    bet = int(input())
    if bet == -1:
        break
    total += bet
    
print(total)
