if __name__ == '__main__':
    S = str(input())
    num = len(S)
    SS = []
    for i in range(num):
        SS.append(S[i:num])
    SS.sort()
    for i in range(num):
        print(SS[i])