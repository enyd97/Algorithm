if __name__ == '__main__':
    num = int(input())
    pos = list(map(int, input().split()))
    if num != 1:
        reach = list(map(int, input().split()))
    can = 0
    tag = 0

    for index in range(num-1):
        if num == 1:
            break
        can = max(can, pos[index] + reach[index])
        if can < pos[index + 1]:
            print("엄마 나 전역 늦어질 것 같아")
            tag = 1
            break
    if not tag:
        print("권병장님, 중대장님이 찾으십니다")