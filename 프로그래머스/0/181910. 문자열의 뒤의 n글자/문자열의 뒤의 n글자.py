def solution(my_string, n):
    str = list(my_string)
    answer = ''.join(str[len(str)-n:])
    return answer