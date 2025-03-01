M = int(input()) 
N = int(input())
prime_list = []

for num in range(M, N+1):
    no_prime = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                no_prime += 1
                break
        if no_prime == 0:
            prime_list.append(num)
            
if len(prime_list) > 0:
    print(sum(prime_list))
    print(min(prime_list))
else:
    print(-1)