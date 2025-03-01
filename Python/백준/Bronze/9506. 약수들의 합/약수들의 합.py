while 1:
    N = int(input())

    if N == -1:
        break;
    num = []
    for i in range(1, N):
        if N % i == 0:
            num.append(i)
    if sum(num) == N:
        print(N, " = ", " + ".join(str(i) for i in num), sep="")
    else:
        print(N, "is NOT perfect.")