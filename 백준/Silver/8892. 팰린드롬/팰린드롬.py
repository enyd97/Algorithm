if __name__ == '__main__':
    N = int(input())
    LL = []
    PP = []

    for i in range(N):
        tag = 0
        T = int(input())
        for j in range(T):
            LL.append(input())
        size = len(LL)
        # LL is list of input strings
        # make all possible cases
        for k in range(size - 1):
            for l in range(k + 1, size):
                tag1 = 0
                tag2 = 0
                current1 = LL[k] + LL[l]
                current2 = LL[l] + LL[k]
                Len = len(current1)
                for m in range(int(Len / 2)):
                    if current1[m] != current1[Len - 1 - m]:
                        tag1 = 1
                        break
                for m in range(int(Len / 2)):
                    if current2[m] != current2[Len - 1 - m]:
                        tag2 = 1
                        break
                if not tag1:
                    tag = 1
                    result = current1
                    break
                if not tag2:
                    tag = 1
                    result = current2
            if tag:
                break
        if tag:
            PP.append(result)
        else:
            PP.append(0)
        LL.clear()
    print(*PP, sep='\n')