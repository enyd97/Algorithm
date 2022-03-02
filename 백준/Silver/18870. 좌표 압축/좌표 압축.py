if __name__ == '__main__':
    len1 = int(input())
    A = list(map(int, input().split()))
    B = sorted(list(set(A)))
    len2 = len(B)
    dic = {}
    for i in range(len2):
        dic[B[i]] = i
    for i in range(len1):
        print(dic[A[i]], end=' ')