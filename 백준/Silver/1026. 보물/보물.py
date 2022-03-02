if __name__ == '__main__':
    num = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0
    A.sort()
    B.sort()

    for i in range(num):
        result += A[i]*B[num-1-i]

    print(result)