if __name__ == '__main__':
    stack = [-1]
    _len = 0
    N = int(input())
    result = []
    for i in range(N):
        current = input().split()
        command = current[0]
        if command == 'push':
            _len = _len + 1
            stack.append(-1)
            stack[_len] = current[1]
        elif command == 'top':
            if _len > 0:
                result.append(stack[_len])
            else:
                result.append(-1)
        elif command == 'pop':
            if _len > 0:
                result.append(stack[_len])
                _len = _len - 1
            else:
                result.append(-1)
        elif command == 'size':
            result.append(_len)
        elif command == 'empty':
            result.append(1 if _len == 0 else 0)
        else:
            pass
    print(*result, sep='\n')