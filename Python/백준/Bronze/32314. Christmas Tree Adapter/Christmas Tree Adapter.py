import sys

a = int(input())  
w, v = map(int, input().split()) 

ampere_candidate = w // v

if ampere_candidate >= a:
    print(1)
else:
    print(0)