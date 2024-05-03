def solution(my_str, n):
    answer = []
    while len(my_str) != 0:
        a = my_str[0:n]
        my_str = my_str[n:]
        answer.append(a)
    return answer