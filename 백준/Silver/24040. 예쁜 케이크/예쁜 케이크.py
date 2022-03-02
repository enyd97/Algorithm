if __name__ == '__main__':
    iteration = int(input())
    result = []
    for _ in range(1, iteration + 1):
        number = int(input())
        if (number - 2) % 3 == 0:
            result.append('TAK')
        elif number % 9 == 0:
            result.append('TAK')
        else:
            result.append('NIE')

    for i in result:
        print(i)
