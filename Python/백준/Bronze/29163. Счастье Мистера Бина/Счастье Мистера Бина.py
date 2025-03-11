import sys

# N : 숫자의 개수
N = int(input())  
numbers = list(map(int, input().split()))  

even_count = sum(1 for x in numbers if x % 2 == 0)
odd_count = N - even_count 

print("Happy" if even_count > odd_count else "Sad")