if __name__ == '__main__':
    N = int(input())
    result = []
    current = []

    for i in range(N):
        count = 0
        tag = 0
        current = input()
        for j in current:
            if j == '(':
                count += 1
            else:
                count -= 1
                if count < 0:
                    tag = 1
        if (count == 0) & (tag == 0):
            result.append('YES')
        else:
            result.append('NO')
    print(*result, sep='\n')