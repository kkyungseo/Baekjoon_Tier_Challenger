import sys

t1, e1, f1 = map(int, input().split())  
t2, e2, f2 = map(int, input().split()) 

time_max = (t1 * 3) + (e1 * 20) + (f1 * 120)
time_mel = (t2 * 3) + (e2 * 20) + (f2 * 120)

if time_max > time_mel:
    print("Max")
elif time_max < time_mel:
    print("Mel")
else:
    print("Draw")