def solution(n, nu):
    answer = []
    for a in nu:
        if a%n == 0:
            answer.append(a)
    return answer