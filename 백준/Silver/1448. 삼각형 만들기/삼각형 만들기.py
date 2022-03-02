if __name__ == '__main__':
    N = int(input())
    list1 = []
    for i in range(N):
        A = int(input())
        list1.append(A)
    list1.sort()
    list1.reverse()
    for i in range(N-2):
        if list1[i] < list1[i+1] + list1[i+2]:
            print(list1[i]+list1[i+1]+list1[i+2])
            exit()
    print(-1)