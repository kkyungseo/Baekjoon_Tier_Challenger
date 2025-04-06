import math

def main():
    n = int(input())
    factorial = math.factorial(n)
    print(factorial % 10)

if __name__ == "__main__":
    main()