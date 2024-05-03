def solution(n):
    answer = 2
    for a in range(1000000):
        if a**2 == n:
            answer = 1
    return answer