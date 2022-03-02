if __name__ == '__main__':
    N, M = input().split()
    N = int(N)
    M = int(M)
    A = ['' for i in range(N)]
    B = ['' for i in range(M)]
    C = ['' for i in range(M)]
    count = 0
    Hash = []
    for i in range(N):
        A[i] = input()

    for j in range(M):
        for i in range(N):
            B[j] += A[i][j]
    for j in range(M-1):
        for i in range(M):
            C[i] = B[i][1:]
        if len(set(C)) == len(B):
            count += 1
            B = C.copy()
        else:
            break
    print(count)