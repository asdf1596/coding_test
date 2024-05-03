def solution(num, total):
    answer = []
    for i in range(total + 1000, -1000, -1) :
        _num = sum([j for j in range(i, i - num, -1)])
        if _num == total : return list(reversed([j for j in range(i, i - num, -1)]))
    return answer